#!/usr/bin/env python3
import argparse
import re
import csv


def contains_domain(address, domain):
    """Returns True if the email address contains the given,domain,in the domain position, false if not."""
    domain = r'[\w\.-]+@' + domain + '$'
    if re.match(domain, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in the received address."""
    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address


def main():
    """Processes the list of emails, replacing any instances of the old domain with the new domain."""
    parser = argparse.ArgumentParser( description='Process a list of emails, replacing instances of the old domain with the new domain.')
    parser.add_argument('-o', '--old_domain', help='Old domain to replace', required=True)
    parser.add_argument('-n', '--new_domain', help='New domain to use', required=True)
    parser.add_argument('-c', '--csv_file_location', help='CSV file location', required=True)
    parser.add_argument('-r', '--report_file', help='Report file location (optional)')
    args = parser.parse_args()

    old_domain, new_domain = args.old_domain, args.new_domain
    csv_file_location = args.csv_file_location
    report_file = args.report_file if args.report_file else 'updated_user_emails.csv'

    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []
    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]
        for email_address in user_email_list:
            if contains_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                replaced_email = replace_domain(email_address, old_domain, new_domain)
                new_domain_email_list.append(replaced_email)
        email_key = ' ' + 'Email Address'
        email_index = user_data_list[0].index(email_key)
        for user in user_data_list[1:]:
            for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
                if user[email_index] == ' ' + old_domain:
                    user[email_index] = ' ' + new_domain
    f.close()
    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()


main()