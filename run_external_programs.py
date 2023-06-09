from subprocess import run, PIPE, CalledProcessError
import shlex

raw_command = "netstat -an"  # command to run

command_words = shlex.split(raw_command)   # command as list of strings

print(f"command_words: {command_words}")

run(command_words)
print('-' * 60)

proc = run(command_words, stdout=PIPE)

raw_output = proc.stdout

output = raw_output.decode()

output_lines = output.splitlines()

for output_line in output_lines:
    if not (('TCP'  in output_line) or ('UDP' in output_line)):
        continue
    if '[' in output_line:
        continue

    if 'ESTABLISHED' in output_line:
        proto, local, remote, _ = output_line.split()
        local_ip, local_port = local.split(':')
        remote_ip, remote_port = remote.split(':')
        print(proto, local_port, remote_port)
        
print('-' * 60)

# cmd = shlex.split(f"copy {file1} {folder}")
# run(cmd)










