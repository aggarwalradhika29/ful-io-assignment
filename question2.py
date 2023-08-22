# libraries
import requests, re
from bs4 import BeautifulSoup

def get_social_links(url):
    """
    Gets the social links from a website.
    Args:
    url: The URL of the website.
    Returns:
    A list of social links.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    social_links = []
    for a in soup.find_all('a', href=True):
        if a['href'].startswith('https://www.'):
            social_links.append(a['href'])
    return social_links


def get_email(url):
    """
    Gets the email address from a website.
    Args:
    url: The URL of the website.
    Returns:
    The email address.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    email_address = soup.find('a', href=re.compile(r'mailto:.*'))['href']
    email_address = email_address.replace('mailto:', '')
    return email_address


def get_contact_number(url):
    """
    Gets the contact number from a website.
    Args:
    url: The URL of the website.
    Returns:
    The contact number.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    contact_number = soup.find('a', href=re.compile(r'tel:.*'))['href']
    contact_number = contact_number.replace('tel:', '')
    return contact_number

def main():
    # Get the URL from the user.
    url = input('Enter the URL of the website: ')

    # Get the social links.
    social_links = get_social_links(url)
    # Get the email address.
    email_address = get_email(url)
    # Get the contact number.
    contact_number = get_contact_number(url)

    # Print the results.
    print('Social links:')
    for social_link in social_links:
        print(social_link)
    print('Email:')
    print(email_address)
    print('Contact:')
    print(contact_number)

if __name__ == '__main__':
    main()
