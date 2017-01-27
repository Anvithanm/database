
import MySQLdb
import re
db=MySQLdb.connect("localhost","root","asm123","info")
cursor=db.cursor()
org_file = open('/home/anvitha/Downloads/diag.out','r')
lis=[]
dicta={}
macdb=[];mackey=[]
for j in org_file:
	a = re.match("----- APmgr info: apmgrinfo -a",j,re.M|re.I)
	if a:
		for j in org_file:
			lis.append(j)
			b = re.match("----- Disconnected APs: wlaninfo --all-disc-ap -l 3", j,re.M|re.I)
			if b:
				break
for i in lis:
	mac = re.findall(r'(?:[\da-fA-F]{2}[:\-]){5}[\da-fA-F]{2}',i,re.I)
	if mac:
		macdb = mac
		mackey.append(mac)
		#print mac
		#result=("insert into prg (Macaddress) values('%s');"%mac[0])
		#cursor.execute(result)
		#db.commit()
	ipv4ad = re.findall(r'(?:[0-9]{3}[:/.]){3}[\d]{1}',i)
	if ipv4ad:
		ipv4db=ipv4ad
		#print ipv4ad
		#res=ipv4ad.split()
		#cursor.execute("insert into prg (IPv4address) values('%s');"%ipv4ad[0])
		#db.commit()
	ipv6ad = re.findall(r'[a-f0-9]{4}::[0-9]',i)
	if ipv6ad:
		ipv6db=ipv6ad
		#print ipv6ad
		#cursor.execute("insert into prg (IPv6address) values('%s');"% ipv6ad[0])
                #db.commit()
	name = re.findall(r'\s*Name\s*:\s(.*)',i)
	if name:
		namedb=name
		#print name
		#cursor.execute("insert into prg (Name) values('%s');"% name[0])
                #db.commit()
	state = re.findall(r'\s*State\s*:\s(.*)',i)
        if state:
		statedb=state
                #print state		
		#cursor.execute("insert into prg (State) values('%s');"% state[0])
                #db.commit()
	tunnel = re.findall(r'\s*Tunnel/Sec Mode\s*:\s*(.*)/',i)
	if tunnel:
		tunneldb=tunnel
		#print tunnel		
		#cursor.execute("insert into prg (Tunnel) values('%s');"% tunnel[0])
                #db.commit()
	secmode = re.match(r'\s.*Tunnel/Sec Mode\s.*:\s(.*)',i)
	if secmode:
		grp = secmode.group(1)
		grp2 = grp.split("/")
		#res = grp2[1]
		#secmodedb=res		
		#print res
		#cursor.execute("insert into prg (Secmode) values('%s');"% res[0])
                #db.commit()
	mesh = re.findall(r'\s*Mesh Role\s*:\s(.*)',i)
	if mesh:
		meshdb=mesh
		#print mesh		
		#cursor.execute("insert into prg (Meshrole) values('%s');"% mesh[0])
                #db.commit()
	psk = re.findall(r'\s*PSK\s*:\s(.*)',i)
        if psk:
		pskdb=psk
                #print psk		
		#cursor.execute("insert into prg (PSK) values('%s');"% psk[0])
                #db.commit()
	timer = re.findall(r'\s*Timer\s*:\s(.*)',i)
        if timer:
		timerdb=timer
                #print timer
		#cursor.execute("insert into prg (Timer) values('%s');"% timer[0])
                #db.commit()
	hwver = re.findall(r'\s*HW/SW Version\s*:\s(.*)/',i)
        if hwver:
		hwverdb=hwver
                #print hwver		
		#cursor.execute("insert into prg (HWversion) values('%s');"% hwver[0])
                #db.commit()
	swver = re.match(r'\s.*HW/SW Version\s.*:\s(.*)',i)
	if swver:
		p = swver.group(1)
		q = p.split("/")
		#res2 = q[1]
		#swverdb=res2
		#print res2		
		#cursor.execute("insert into prg (SWversion) values('%s');"% res2[0])
                #db.commit() 
	model = re.findall(r'\s*Model/Serial Num\s*:\s(.*)/',i)
        if model:
		modeldb=model
		#print model
		#cursor.execute("insert into prg (Model) values('%s');"% model[0])
                #db.commit()
	serialno = re.match(r'\s.*Model/Serial Num\s.*:\s(.*)',i)
       	if serialno:
                r = serialno.group(1)
                s = r.split("/")
		#res3 = s[1]
		#serialdb=res3
                #print res3
		
		#cursor.execute("insert into prg (Serialnumber) values('%s');"% res3[0])
                #db.commit()
		dicta[macdb[0]]=[macdb[0],ipv4db[0],ipv6db[0],namedb[0],statedb[0],tunneldb[0],grp2[1],meshdb[0],pskdb[0],timerdb[0],hwverdb[0],q[1],modeldb[0],s[1]]
for k in mackey:
	aa=k[0]
	if aa in dicta:
		bb=dicta[aa]
		cursor.execute("""insert into prg values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(bb[0],bb[1],bb[2],bb[3],bb[4],bb[5],bb[6],bb[7],bb[8],bb[9],bb[10],bb[11],bb[12],bb[13]))
db.commit()
cursor.execute("select * from prg")
#rows=cursor.fetchall()
#for row in rows:
	#print row
		
org_file.close()


