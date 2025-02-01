# gpt_partition_parser

This is a python tool to do GPT partition table parsing. It lists the detail information with a given image file:

```java
python gptheader-read.py gpt_main0.bin
GPT Header:
Signature: EFI PART
Revision: 65536
Header Size: 92
Header CRC32: 2087626444
Reserved: 0
Current LBA: 1
Backup LBA: 22184236
First Usable LBA: 6
Last Usable LBA: 22184231
Disk GUID: b'\xc2E<\x04\xb2z\x9c\xd4\xb4\xd2\xc6\x88w\xf4.\xe6'
Partition Entries Starting LBA: 2
Number of Partition Entries: 64
Size of Partition Entry: 128
Partition Entries CRC32: 3100194116
Total LBAs in LUN: 22184237
Partition Entry Size: 128
Number of Partition Entries: 64
Partition Entries Offset: 1024
Warning: Partition entries CRC32 mismatch

Partition Entries:
Partition 25:
  Partition Type GUID: b'EFI PART\x00\x00\x01\x00\\\x00\x00\x00'
  Unique Partition GUID: b'\xcc\xa6n|\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00'
  First LBA: 22184236
  Last LBA: 6
  Attributes: 22184231
  Partition Name: 
  Offset of GUID: 4096
Partition 57:
  Partition Type GUID: b'\x08J>\x13\xefM\xe6\x11\xbe\xb8\x9eq\x12\x8c\xaew'
  Unique Partition GUID: b'\xd7|\x06\xfa\x90O\xc5\xac\x07\xdf-~m\xc0\xd7\xf5'
  First LBA: 6
  Last LBA: 65541
  Attributes: 1152921504606846976
  Partition Name: ifs2_a
  Offset of GUID: 8192
Partition 58:
  Partition Type GUID: b'\x08J>\x13\xefM\xe6\x11\xbe\xb8\x9eq\x12\x8c\xaew'
  Unique Partition GUID: b'A\xcb\x08\xeb\xac\x1c\xb6\x88\xf1\xbe\n\x97&Rx\x97'
  First LBA: 65542
  Last LBA: 131077
  Attributes: 1152921504606846976
  Partition Name: ifs2_b
  Offset of GUID: 8320
Partition 59:
  Partition Type GUID: b'QZ\x06:\xc6\x809D\x86\x02yCp#c*'
  Unique Partition GUID: b'\xa7cwDDv\xc2q\xa4W\n\x19#-\xe9d'
  First LBA: 131078
  Last LBA: 1048581
  Attributes: 1152921504606846976
  Partition Name: system_a
  Offset of GUID: 8448
Partition 60:
  Partition Type GUID: b'QZ\x06:\xc6\x809D\x86\x02yCp#c*'
  Unique Partition GUID: b'\xaf\x04\xe1\xb4\x18\xb1\xb1\xea\xdf\xb4e(\xb0\xf9\xd3^'
  First LBA: 1048582
  Last LBA: 1966085
  Attributes: 1152921504606846976
  Partition Name: system_b
  Offset of GUID: 8576
Partition 61:
  Partition Type GUID: b'\xe6\xe7\x81\x1b\r\xf5\x9bA\xa79*\xee\xf8\xad3T'
  Unique Partition GUID: b'~\x08`\x92\xd6o\x1e\tW\xfa\xabr\xb0\x9ehn'
  First LBA: 1966086
  Last LBA: 3014661
  Attributes: 1152921504606846976
  Partition Name: hmi_data_a
  Offset of GUID: 8704
Partition 62:
  Partition Type GUID: b'\xe6\xe7\x81\x1b\r\xf5\x9bA\xa79*\xee\xf8\xad3T'
  Unique Partition GUID: b'\xc7>\xdb(\\l\xa9W\xe8\x95\xc3\xf6\xdf[\x0e\x92'
  First LBA: 3014662
  Last LBA: 4063237
  Attributes: 1152921504606846976
  Partition Name: hmi_data_b
  Offset of GUID: 8832
Partition 63:
  Partition Type GUID: b'\xf1G\xb7l\xef\xc2\x92@\xad\xd0\xca9\xf7\x9cz\xf4'
  Unique Partition GUID: b'\xbfAq\xb5\x03\xff\x92T\x88\xad|h\x06\xd9\xa3K'
  First LBA: 4063238
  Last LBA: 4063749
  Attributes: 1152921504606846976
  Partition Name: bluetooth_a
  Offset of GUID: 8960
Partition 64:
  Partition Type GUID: b'\xf1G\xb7l\xef\xc2\x92@\xad\xd0\xca9\xf7\x9cz\xf4'
  Unique Partition GUID: b'K\xb1\x84-\x85\xdb1TGE\x1b+\xafC\xbb\xa4'
  First LBA: 4063750
  Last LBA: 4064261
  Attributes: 1152921504606846976
  Partition Name: bluetooth_b
  Offset of GUID: 9088

```