from tempfile import TemporaryFile
f = TemporaryFile('w+')
f.write("Hellonihaoa")
# f.seek(0)
data = f.readlines()
print(data)