from datetime import datetime


now=datetime.now()
h=int(now.strftime('%H'))
se=int(now.strftime('%M'))

seconde=h*60+se

print(h,':',se)
print(seconde)
