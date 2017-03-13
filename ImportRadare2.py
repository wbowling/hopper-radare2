import r2pipe

doc = Document.getCurrentDocument()
segment = doc.getCurrentSegment()

r2p = r2pipe.open(doc.getExecutableFilePath())
r2p.cmd('aaa')
r2functions = r2p.cmdj('aflj')
r2p.quit()

for r2function in r2functions:
    doc.setNameAtAddress(r2function['offset'], r2function['name'])
