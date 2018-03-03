import re
import sys

forbidden_action = ["SCHEDULER_EXECUTOR_SESSION_START",
                    "SCHEDULER_EXECUTOR_SESSION_END",
                    "SCHEDULER_CONNECTIVITY_CHECK_DEBUG",
                    "SCHEDULER_WAKEUP",
                    "SCHEDULER_WAKEUP_BATCH",
                    "SCHEDULER_WAKEUP_COMPLETE",
                    "SCHEDULER_WAKEUP_COMPLETE_BATCH",
                    "DOWNLOAD_SIZE_PREDICTION",
                    "REAUTH_SETTINGS_FROM_DEVICE",
                    "PLAYSHIELD_SIGNALS",
                    "ACQUIRE_CACHE_INSTANTIATE",
                    "ACQUIRE_CACHE_BLACKLIST_RETRIEVE",
                    "ACQUIRE_CACHE_RETRIEVE",
                    "INSTALL_SCHEDULED",
                    "PAGE_LOAD_START",
                    "PAGE_LOAD_END",
                    "PAGE_LOAD_FIRST_RPC_INITIATED",
                    "PAGE_LOAD_LAST_RPC_COMPLETED",
                    "JANK_REPORT",
                    "VERIFY_APPS_VERIFY_INSTALL",
                    "MAIN_ACTIVITY_ON_STOP",
                    "MAIN_ACTIVITY_ON_READY",
                    "MAIN_ACTIVITY_ON_START",
                    "VERIFY_APPS_BEGIN_INSTALL_VERIFICATION",
                    "CLICK_TRACKING_ERROR_DEEP_LINK"]


def extract_parent_id(line):
  pattern = re.search(".*parent_client_id: ([0-9]*)", line)
  if pattern:
    return pattern.group(1)


def extract_client_id(line):
  pattern = re.search("[ ]+client_id: ([0-9]*)", line)
  if pattern:
    return pattern.group(1)
  else:
    return


def has_parented_client_id(line, parent_ids):
  client_id = extract_client_id(line)
  parent_id = extract_parent_id(line)
  if parent_id is not None:
    return True
  if client_id is None:
    return False
  else:
    return client_id in parent_ids


def get_parent_ids(file_name):
  parent_ids = set()
  with open(file_name, 'r') as fp:
    for line in fp:
      id = extract_parent_id(line)
      if id is not None:
        parent_ids.add(id)
  return parent_ids


def get_bg_event_type(line):
  pattern = re.search(".*type: (.*)", line)
  return pattern.group(1)


def qualify(line):
  return not re.match(".*target_id:.*", line)


def write_file(out_file, lines, ind_start, ind_end):
  for i in range(ind_start, ind_end):
    if qualify(lines[i]):
      out_file.write(lines[i])


def output_block(out_file, original_lines, ind_start, ind_end):
  print("output file " + str(ind_start) + ", " + str(ind_end))
  i = ind_start
  while i < ind_end:
    # if qualify(original_lines[i]) and not re.match(".*background_action {.*"):
    #   out_file.write(original_lines[i])
    if re.match(".*background_action {.*", original_lines[i]):
      should_skip_bg_action = get_bg_event_type(original_lines[i + 1]) in forbidden_action
      left_bracket = 1
      bg_start = i
      bg_end = i
      while left_bracket > 0:
        bg_end += 1
        if re.match(".*}.*", original_lines[bg_end]):
          left_bracket -= 1
        elif re.match(".*{.*", original_lines[bg_end]):
          left_bracket += 1
      # if out of bound, continue with normal process
      if bg_end + 1 > ind_end:
        write_file(out_file, original_lines, i, i + 1)
        i += 1
      # write or skip bg action and assign index to end of it
      else:
        if not should_skip_bg_action:
          write_file(out_file, original_lines, bg_start, bg_end + 1)
        i = bg_end + 1
    else:
      write_file(out_file, original_lines, i, i + 1)
      i += 1


def trim_logs(input_file_name, output_file_name):
  parent_ids = get_parent_ids(input_file_name)
  with open(input_file_name, 'r') as input, open(output_file_name, 'w') as output:
    lines = input.readlines()
    size = len(lines)
    valid = True
    i = 0
    pre_event_start = 0
    while i < size:
      if re.match(".*Event {.*", lines[i]):
        if valid:
          output_block(output, lines, pre_event_start, i)
        pre_event_start = i
        valid = False
      else:
        if has_parented_client_id(lines[i], parent_ids):
          valid = True
      i += 1
    output_block(output, lines, pre_event_start, size)


trim_logs("/Users/ruoyu/Desktop/logs/dl_search_acq_session.txt",
          "/Users/ruoyu/Desktop/trimmed_logs/dl_search_acq_session_trimmed.txt")
