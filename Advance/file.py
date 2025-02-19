# File Objects
print('\n-------------------FILE READ AND WRITE-----------------\n')

## Read Method 1
f = open('File manipulation/file.txt', 'r')
print('The name of file is -', f.name)
print('The mode of file is -', f.mode)
print()
f.close()

## Read Method 2
with open('File manipulation/file.txt', 'r') as rf:
    # whole_content = rf.read()
    # print(whole_content)

    # one_line = rf.readline()
    # print(one_line)

    # arr_lines = rf.readlines()
    # print(arr_lines)

    # for line in rf:
    #     print(line, end='')

    size_to_read = 10
    f_contents = rf.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = rf.read(size_to_read)
    
    print('Cursor is at -', rf.tell())
    rf.seek(0)
    print('After Seek, Cursor is at -', rf.tell())
    
## Write Mode
with open('File manipulation/file2.txt', 'w') as wf:
    wf.write('WRITE OPERATION')
    wf.write('\nTesting write operation from file.py')
    wf.write('\nThis text has come from File Read and Write section!')
    print('\nWRITE Operation on file2.txt performed successfully')

## Append Mode
with open('File manipulation/file2.txt', 'a') as af:
    af.write('\nAPPEND OPERATION')
    af.write('\nThis line is appended after the Write Operation.')
    print('\nAPPEND Operation on file2.txt performed successfully')

## Read and Write binary files. [IMAGE COPY]
with open('File manipulation/Penguin.png', 'rb') as img:
    with open('File manipulation/Penguin_Copy.png', 'wb') as copy:
        chunk_size = 4096
        img_chunk = img.read(chunk_size)
        while len(img_chunk) > 0:
            copy.write(img_chunk)
            img_chunk = img.read(chunk_size)
        print('\nPenguin.png photo copied successfully.')

