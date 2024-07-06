from ClassiPyGRB import SWIFT

swift = SWIFT(root_path=r'data', res=64)
df = swift.summary_table()