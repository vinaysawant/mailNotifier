#!/usr/bin/python
import imaplib
import sys
 
IMAP_SERVER='imap.gmail.com'
IMAP_PORT=993
 
M = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

rc, resp = M.login('email@gmail.com', 'Password')
print rc, resp

while 1:

	M.SELECT('INBOX')

	status, response = M.status('INBOX', "(UNSEEN)")  #count the unread mails
	unreadcount = int(response[0].split()[2].strip(').,]'))

	if unreadcount <> 0: 							 #if new mails received then notify user
		print "You have %s new mail " %unreadcount 
		
		status, email_ids = M.search(None, '(UNSEEN)')
	
		def get_details(email_ids):					# for getting details of the email
			details = []
	   		for e_id in email_ids:
   				_, response = M.fetch(e_id, '(body[header.fields (subject from)])')
				details.append( response[0][1][9:] )
   			return details
	
		if unreadcount == 1:
			for email in get_details(email_ids):
		  			print 'With following details \n' + email
	
		

		def exit():
			M.logout()
			sys.exit()
