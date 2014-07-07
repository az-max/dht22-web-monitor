#!/usr/bin/env python

import sqlite3
import sys
import cgi
import cgitb


# global variables
speriod=(15*60)-1
dbname='/var/www/templog2.db'
table=24


# print the HTTP header
def printHTTPheader():
    print "Content-type: text/html\n\n"



# print the HTML head section
# arguments are the page title and the table for the chart
def printHTMLHead(title, table):
    print "<head>"
    print "    <title>"
    print title
    print " </title>"
    print
    print "<script src=http://code.jquery.com/jquery-1.11.0.min.js></script>"
    print "<script src=/js/raphael.2.1.0.min.js></script>"
    print "<script src=/js/justgage.1.0.1.min.js></script>"
    print "<meta http-equiv=",'"refresh"'," content=",'"600"',">"

    print "</head>"

# connect to the db and show some stats
# argument option is the number of hours
def show_stats(option):

    global rowstrcurrtmp
    global rowstrcurrhum
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    if option is None:
        option = str(24)
    curs.execute("SELECT temp,humidity FROM Temps WHERE datestamp = (SELECT max( datestamp ) FROM temps) and   timestamp= (select max(timestamp) from temps where datestamp = (SELECT max( datestamp ) FROM temps))")
    rowcurrent=curs.fetchone()
    rowstrcurrtmp="{0:.1f}".format(rowcurrent[0])
    rowstrcurrhum="{0}".format(str(rowcurrent[1]))

    conn.close()


# check that the option is valid
# and not an SQL injection
def validate_input(option_str):
    # check that the option string represents a number
    if option_str.isalnum():
        # check that the option is within a specific range
        if int(option_str) > 0 and int(option_str) <= 24:
            return option_str
        else:
            return None
    else: 
        return None


#return the option passed to the script
def get_option():
    form=cgi.FieldStorage()
    if "timeinterval" in form:
        option = form["timeinterval"].value
        return validate_input (option)
    else:
        return None

# justgage script

def print_graph_temp(temp,humidity):
    
    print "<script>"
    print "var g = new JustGage({"
    print "id:",'"tempgauge"',","
    print "value:", temp,","
    print "min: 50,"
    print "max: 100,"
    print "title:",'"Temperature"',","
    print "label:",'"Fahrenheit"'
    print "});"
    print "</script>"
# humidity
    print "<script>"
    print "var g = new JustGage({"
    print "id:",'"humiditygauge"',","
    print "value:", humidity,","
    print "min: 0,"
    print "max: 100,"
    print "title:",'"Humidity"',","
    print "levelColorsGradient: true,"
    print "label:",'"Percent"'
    print "});"
    print "</script>"





def show_graph():
    print "<table>"
    print "<tr>"
    print '<td><div id="tempgauge" style="width:200px; height:160px" </div></td>'
    print '<td><div id="humiditygauge" style="width:200px; height:160px"></div></td>'
    print "</tr>"
    print "</table>"

# main function
# This is where the program starts 
def main():

    cgitb.enable()

    # get options that may have been passed to this script
    option=get_option()

    if option is None:
        option = str(24)

    # print the HTTP header
    printHTTPheader()

    
    # start printing the page
    print "<html>"
    # print the head section including the table
    # used by the javascript for the chart
    printHTMLHead("Raspberry Pi Temperature Logger", table)

    # print the page body
    print "<body>"
    print "<h1>Raspberry Pi Temperature Logger</h1>"
    print "<hr>"
    show_stats(option)
#    print_graph_temp(rowstrcurrtmp)
    show_graph()
    print_graph_temp(rowstrcurrtmp,rowstrcurrhum)
    print "</body>"
    print "</html>"

    sys.stdout.flush()

if __name__=="__main__":
    main()
