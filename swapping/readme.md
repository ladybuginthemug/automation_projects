
### to swap file extensions in bulk:
run `./extension-swap.sh`
```commandline

Usage: extension-swap.sh [-f filename] [-e extension] [-n new_extension] [-h help]

Options:
  -f filename       Specify a specific filename to search for 
  -e extension      Specify the file extension to search for 
  -n new_extension  Specify the new file extension to rename to 

```

### to swap email domains in bulk:
run `python3 replace_domain.py`

```commandline

usage: replace_domain.py [-h] -o OLD_DOMAIN -n NEW_DOMAIN -c CSV_FILE_LOCATION [-r REPORT_FILE]

Process a list of emails, replacing instances of the old domain with the new domain.

options:
  -h, --help            show this help message and exit
  -o OLD_DOMAIN, --old_domain OLD_DOMAIN
                        Old domain to replace
  -n NEW_DOMAIN, --new_domain NEW_DOMAIN
                        New domain to use
  -c CSV_FILE_LOCATION, --csv_file_location CSV_FILE_LOCATION
                        CSV file location
  -r REPORT_FILE, --report_file REPORT_FILE
                        Report file location (optional)

```