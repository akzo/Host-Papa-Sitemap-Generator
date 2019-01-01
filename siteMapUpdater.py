# establishing ftp connection
# link to the api
from ftplib import FTP
import os

def upload_to_hostPapa(ftpHost, account, password, sitemapName):
    
    ftp = FTP(ftpHost, account, password)
    ftp.cwd('public_html')
    sitemap = open(sitemapName, 'rb')
    ftpStoreCommand = 'STOR ' + sitemapName
    ftp.storbinary(ftpStoreCommand, sitemap)
    sitemap.close()
    ftp.quit()

    print('Sitemap was successfully uploaded')
    
def createSiteMap(website):
    os.system("python mySiteMap\\main.py --domain %s --output sitemap.xml --debug" % website);


website = input('Enter a link for the website: ')
ftpLink = input('Enter ftp link: ')
ftpAccount = input('Enter ftp account: ')
ftpPassword = input('Enter ftp password: ')
createSiteMap(website)
upload_to_hostPapa(ftpLink, ftpAccount, ftpPassword, "sitemap.xml")


