from collections import deque

DATA = [("1255", "Abi"), ("1256", "Yahya"), ("1257", "Muhammad")]

def demo_array():
    array_mhs = []                          
    for nim, nama in DATA:
        array_mhs.append((nim, nama))       
    print("Data berurutan (Array):", array_mhs)
    print("Akses indeks ke-1     :", array_mhs[1])   

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None                    


class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_depan(self, data):          
        node = Node(data)
        node.next = self.head
        self.head = node

    def hapus_depan(self):                  
        if self.head:
            self.head = self.head.next

    def hapus_by_nim(self, nim):            
        cur, prev = self.head, None
        while cur:
            if cur.data[0] == nim:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return
            prev, cur = cur, cur.next

    def tampil(self):
        cur, hasil = self.head, []
        while cur:
            hasil.append(cur.data)
            cur = cur.next
        return hasil

def demo_linked_list():
    ll = LinkedList()                       
    for d in DATA:
        ll.tambah_depan(d)
    print("Setelah menambah data :", ll.tampil())
    ll.hapus_depan()
    print("Setelah hapus head    :", ll.tampil())

class Stack:
    def __init__(self):
        self.items = []                     

    def push(self, x):
        self.items.append(x)              

    def pop(self):
        return self.items.pop() if self.items else None   

    def peek(self):
        return self.items[-1] if self.items else None     

    def is_empty(self):
        return not self.items


def demo_stack_undo():
    riwayat = Stack()
    for nim, nama in DATA:
        riwayat.push(f"tambah {nama}")      
    print("Aksi terakhir (peek)  :", riwayat.peek())
    print("UNDO ->", riwayat.pop())          
    print("UNDO ->", riwayat.pop())

class Queue:
    def __init__(self):
        self.items = deque()                

    def enqueue(self, x):
        self.items.append(x)                

    def dequeue(self):
        return self.items.popleft() if self.items else None   

    def is_empty(self):
        return not self.items


def demo_queue():
    antrean = Queue()
    for d in DATA:
        antrean.enqueue(d)
    while not antrean.is_empty():
        print("Diproses (FIFO)       :", antrean.dequeue())

def demo_hash_table():
    tabel = {nim: nama for nim, nama in DATA}   
    print("Cari NIM 1257         :", tabel.get("1257"))   
    print("Cari NIM 9999         :", tabel.get("9999"))

if __name__ == "__main__":
    print("== ARRAY: menyimpan data berurutan di memori ==")
    demo_array()
    print("\n== LINKED LIST: menambah & menghapus data ==")
    demo_linked_list()
    print("\n== STACK: menumpukkan data / fitur Undo ==")
    demo_stack_undo()
    print("\n== QUEUE: antrean pengolahan data ==")
    demo_queue()
    print("\n== HASH TABLE: pencarian berdasarkan key ==")
    demo_hash_table()
