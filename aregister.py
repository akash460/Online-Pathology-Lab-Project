#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
cur.execute("select * from dregister")
t=cur.fetchall()
print("""
<html>
<head>
<link rel="stylesheet" type="text/css" href="table.css">
<head>
<body style="background-color:#006699;>
 <center> <font size = "5" color="CCCCCC">
<img src="logo1.png" style="width:100%;height:150px">
<table font-size="5">
<tr>
<td> <a href="index.html">Home</a></td>
<td> <a href="plogin.html">Patient</a></td>
<td> <a href="dlogin.html">Doctors</a></td>
<td> <a href="aregister.py">Appoinment</a></td>
</tr>
</table>
<br> 
    <h1>Appointment details of Patient</h1><br>
    <h4><p>Please fill in this form, we will contact you soon.</p></h4></center><br>
	 
	 

<form action="aregstoring.py">

<div style="width: 52%; float: left;">
<input type="text" name="a" value="" size="75"  aria-required="true" placeholder="Name"><br><br>
<input type="email" name="b" value="" size="75"  aria-required="true" placeholder="Email"><br><br>
<input type="tel" name="c" value="" size="75"  aria-required="true" placeholder="Phone"><br><br>
<textarea name="d" cols="60" rows="10" placeholder="Special notes, concerns, or requirements"></textarea><br><br>
<input type="submit" value="Request My Appointment" >
</div>

<div style="width: 48%; float: right; float: up;">
<font size = "6" color="CCCCCC" >	 What is the best way to reach you?<br> <br>
<input type="radio" name="e" value="Phone">Phone<input type="radio" name="e" value="Email">Email<br><br>
<font size = "6" color="CCCCCC" >	 Days of the week you are available for appointment:<br><br> 
<input type="radio" name="f" value="Monday">Monday<input type="radio" name="f" value="Tuesday">Tuesday<input type="radio" name="f" value="Wednesday">Wednesday<input type="radio" name="f" value="Thursday">Thursday<input type="radio" name="f" value="Friday">Friday<br><br>
<font size = "6" color="CCCCCC" >	 Best time of day for your appointment:<br> <br>
<input type="radio" name="g" value="Morning">Morning<input type="radio" name="g" value="Afternoon">Afternoon<br><br>
</div>
<table>
<tr>
""")
for i in t:
        print(
            """<td><b><input type="radio" name="j" value="%s"> %s <br>  %s <br> specialisation: %s <br><br></b></td>""" %(i[3],i[1],i[6],i[7]))
            
print(""" 
</tr>
</table>
</form>                 
</body>
</html>
""")