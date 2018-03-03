import re


def get_meaningful_part(line):
  pattern = re.search("(.*)[\t]+#.*", line)
  if pattern is not None:
    return pattern.group(1) + '\n'
  else:
    return line


def delete_sharp(input_file_name, output_file_name):
  with open(input_file_name, 'r') as input, open(output_file_name, 'w') as output:
    for line in input:
      output.write(get_meaningful_part(line))


delete_sharp("/Users/ruoyu/Desktop/test_pspv.txt",
             "/Users/ruoyu/Desktop/corrected_pspv.txt")
