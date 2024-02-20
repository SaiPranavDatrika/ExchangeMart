from pyravendb.store import document_store

# Set up RavenDB document store
class USERS:
     
     def __init__(self,username,password,address) -> None:
          self.username=username
          self.password=password
          self.address=address
store = document_store.DocumentStore(urls=["https://a.exchangemart.ravendb.community:8080"], database="Exchangemart")
store.initialize()
session = store.open_session()

Users=USERS("SaiPranav",12345,"San Marcos, Texas, USA")
session.store(Users)
session.save_changes()
session.close()

# Perform operations with the document store
# For example, store.open_session(), store.execute_index(), etc.

# Don't forget to dispose of the store when done

