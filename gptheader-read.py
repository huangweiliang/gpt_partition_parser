import struct
import sys
import zlib

GPT_HEADER_FORMAT = '<8sIIIIQQQQ16sQIII'
GPT_PARTITION_ENTRY_FORMAT = '<16s16sQQQ72s'
EXPECTED_SIGNATURE = b'EFI PART'

def read_gpt_header(file, offset):
    file.seek(offset)
    header_data = file.read(92)  # GPT header size is 92 bytes
    if len(header_data) != 92:
        raise ValueError("Failed to read GPT header")
    return struct.unpack(GPT_HEADER_FORMAT, header_data), header_data

def read_partition_entries(file, header):
    partition_entries = []
    partition_entry_size = header[12]
    num_partition_entries = header[11]
    partition_entries_offset = header[10] * 512  # Partition entries start at LBA specified in header

    print("Partition Entry Size: {}".format(partition_entry_size))
    print("Number of Partition Entries: {}".format(num_partition_entries))
    print("Partition Entries Offset: {}".format(partition_entries_offset))

    file.seek(partition_entries_offset)
    partition_entries_data = file.read(partition_entry_size * num_partition_entries)
    if len(partition_entries_data) != partition_entry_size * num_partition_entries:
        raise ValueError("Failed to read partition entries")

    for i in range(num_partition_entries):
        entry_data = partition_entries_data[i * partition_entry_size:(i + 1) * partition_entry_size]
        partition_entries.append(struct.unpack(GPT_PARTITION_ENTRY_FORMAT, entry_data))
    return partition_entries, partition_entries_data

def is_empty_partition(entry):
    return all(field == 0 or field == b'\x00' * len(field) for field in entry)

def parse_gpt(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Read the primary GPT header at offset 0x1000 (4096 bytes)
            header, header_data = read_gpt_header(file, 0x1000)
            if header[0] != EXPECTED_SIGNATURE:
                print("Error: Invalid GPT header signature")
                print("  Found: {}".format(header[0]))
                print("  Expected: {}".format(EXPECTED_SIGNATURE))

            # Verify GPT header CRC32
            header_crc32 = header[3]
            header_data_without_crc = header_data[:16] + b'\x00\x00\x00\x00' + header_data[20:]
            calculated_header_crc32 = zlib.crc32(header_data_without_crc) & 0xFFFFFFFF
            if header_crc32 != calculated_header_crc32:
                print("Warning: GPT header CRC32 mismatch")

            print("GPT Header:")
            print("Signature: {}".format(header[0].decode()))
            print("Revision: {}".format(header[1]))
            print("Header Size: {}".format(header[2]))
            print("Header CRC32: {}".format(header[3]))
            print("Reserved: {}".format(header[4]))
            print("Current LBA: {}".format(header[5]))
            print("Backup LBA: {}".format(header[6]))
            print("First Usable LBA: {}".format(header[7]))
            print("Last Usable LBA: {}".format(header[8]))
            print("Disk GUID: {}".format(header[9]))
            print("Partition Entries Starting LBA: {}".format(header[10]))
            print("Number of Partition Entries: {}".format(header[11]))
            print("Size of Partition Entry: {}".format(header[12]))
            print("Partition Entries CRC32: {}".format(header[13]))

            # Calculate and print total LBAs
            total_lbas = header[6] + 1
            print("Total LBAs in LUN: {}".format(total_lbas))

            partition_entries, partition_entries_data = read_partition_entries(file, header)

            # Verify partition entries CRC32
            partition_entries_crc32 = header[13]
            calculated_partition_entries_crc32 = zlib.crc32(partition_entries_data) & 0xFFFFFFFF
            if partition_entries_crc32 != calculated_partition_entries_crc32:
                print("Warning: Partition entries CRC32 mismatch")

            print("\nPartition Entries:")
            for i, entry in enumerate(partition_entries):
                if is_empty_partition(entry):
                    continue
                partition_type_guid = entry[0]
                unique_partition_guid = entry[1]
                first_lba = entry[2]
                last_lba = entry[3]
                attributes = entry[4]
                try:
                    partition_name = entry[5].decode('utf-16-le').rstrip('\x00')
                except UnicodeDecodeError:
                    partition_name = "<Invalid UTF-16>"
                print("Partition {}:".format(i + 1))
                print("  Partition Type GUID: {}".format(partition_type_guid))
                print("  Unique Partition GUID: {}".format(unique_partition_guid))
                print("  First LBA: {}".format(first_lba))
                print("  Last LBA: {}".format(last_lba))
                print("  Attributes: {}".format(attributes))
                print("  Partition Name: {}".format(partition_name))
                print("  Offset of GUID: {}".format(header[10] * 512 + i * header[12]))
    except Exception as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gptheader-read.py <binary_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    parse_gpt(file_path)