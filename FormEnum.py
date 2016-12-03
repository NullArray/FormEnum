import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('user-agent', '  Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3'),
('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]

try:
    while True:
        url = raw_input("Input target URL: ")

        try:
            br.open(url)
        except:
            print "\n [!]Could not open page, exiting."
            break

        for form in br.forms():
            print "Form name:", form.name
            print form

except KeyboardInterrupt:
	break
	print "\n [!]Critical, user aborted script."
