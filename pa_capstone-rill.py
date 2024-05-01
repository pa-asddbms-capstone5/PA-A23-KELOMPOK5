import pwinput
import os
from prettytable import prettytable
import mysql.connector
import random
import time

#--------Common---------#
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Server lokal jika terjadi error
# def conn():
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root", 
#             password="",
#             database="paasd"
#         )
#         return connection
#     except:
#         input("Error:")

def conn():
    try:
        connection = mysql.connector.connect(
            host="103.54.170.117",
            user="paasd", 
            password="Paasd1234!",
            database="paasd"
        )
        return connection
    except:
        input("Error:")


def err_conn(err):
    
    input("Gagal membuat akun user.")
    clear()
    return

#--------------------Object-----------------#
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0  # Menambahkan atribut _size untuk menyimpan jumlah elemen dalam linked list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1  # Menambahkan 1 ke _size setiap kali sebuah elemen ditambahkan

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
        
    def size(self):
        return self._size


class EkosistemDarat:
    def __init__(self):
        self.connection = conn()
        self.ekosistem_list = DoubleLinkedList()

    def get_mid(self, head):
        if head is None:
            return None
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge_sort(self, head, order='asc'):
        if head is None or head.next is None:
            return head
        
        middle = self.get_mid(head)
        next_to_middle = middle.next
        
        middle.next = None
        
        left = self.merge_sort(head, order)
        right = self.merge_sort(next_to_middle, order)
        
        sorted_list = self.merge(left, right, order)
        return sorted_list

    def merge(self, left, right, order='asc'):
        result = None
        
        if left is None:
            return right
        if right is None:
            return left
        
        if order == 'asc':
            if left.data[0] <= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        elif order == 'desc':
            if left.data[0] >= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        
        return result

    def search(self, id_admin):
        if not self.connection:
            input("Tidak dapat terhubung ke database.")
            self.menu(id_admin)

        try:
            cursor = self.connection.cursor()
            target = input("Masukkan nama ekosistem yang ingin dicari: ")
            query = "SELECT * FROM ekosistem_darat WHERE nama_ekosistem LIKE %s"
            cursor.execute(query, ("%" + target + "%",))
            results = cursor.fetchall()
            if results:
                table = prettytable.PrettyTable(["id_ekosistem", "nama_ekosistem", "id_admin", "lokasi_geografis", "status_ekosistem"])
                for result in results:
                    table.add_row(result)
                print("Data ditemukan:")
                print(table)
            else:
                input("~~~~~DATA TIDAK DITEMUKAN!!!!!~~~~~.")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        except:
            
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        finally:
            if cursor:
                cursor.close()


    def create(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                nama_ekosistem = input("\nMasukkan nama ekosistem: ")
                lokasi_geografis = input("Masukkan lokasi geografis: ")
                status_ekosistem = input("Masukkan status ekosistem: ")

                query = "INSERT INTO ekosistem_darat (nama_ekosistem, lokasi_geografis, id_admin, status_ekosistem) VALUES (%s, %s, %s, %s)"
                data = (nama_ekosistem, lokasi_geografis, id_admin, status_ekosistem)
                cursor.execute(query, data)

                self.connection.commit()
                print("|         -----------------------------------------------------       |")
                print("|          Berhasil Memasukan Data ke Database Ekosistem Darat        |")
                print("|         -----------------------------------------------------       |")
                # Menambah data ke dalam linked list
                self.ekosistem_list.append((cursor.lastrowid, nama_ekosistem, id_admin, lokasi_geografis, status_ekosistem))
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|            Gagal Memasukan Data ke Database Ekosistem Darat         |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
                self.connection.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def read(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM ekosistem_darat"
                cursor.execute(query)
                ekosistem_darat = cursor.fetchall()
                if ekosistem_darat:
                    table = prettytable.PrettyTable(["id_ekosistem", "nama_ekosistem", "id_admin", "lokasi_geografis", "status_ekosistem"])
                    for ekosistem in ekosistem_darat:
                        table.add_row(ekosistem)
                        # Menambah data ke dalam linked list
                        self.ekosistem_list.append(ekosistem)
                    print(table)
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|                   Data Ekosistem Darat Tidak Tersedia               |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                cursor.close()
            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                   Data Spesies Tumbuhan Gagal Dibaca                |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def read_by_user(self, id_user):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM ekosistem_darat"
                cursor.execute(query)
                ekosistem_darat = cursor.fetchall()
                if ekosistem_darat:
                    table = prettytable.PrettyTable(["id_ekosistem", "nama_ekosistem", "id_admin", "lokasi_geografis", "status_ekosistem"])
                    table._max_width = {"id_ekosistem": 3, "nama_ekosistem": 30, "id_admin": 3, "lokasi_geografis": 40, "status_ekosistem": 20}
                    for ekosistem in ekosistem_darat:
                        table.add_row(ekosistem)
                        # Menambah data ke dalam linked list
                        self.ekosistem_list.append(ekosistem)
                    print(table)
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    menu_user(id_user)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|                   Data Ekosistem Darat Tidak Tersedia               |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    menu_user(id_user)
                cursor.close()
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                   Data Ekosistem Darat Gagal Dibaca                 |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                menu_user(id_user)
            finally:
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            menu_user(id_user)

    def update(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                id_ekosistem = input("Masukkan ID ekosistem darat yang akan diupdate: ")
                select_query = "SELECT * FROM ekosistem_darat WHERE id_ekosistem = %s"
                cursor.execute(select_query, (id_ekosistem,))
                ekosistem_data = cursor.fetchone()
                if ekosistem_data:
                    table = prettytable.PrettyTable(["id_ekosistem", "nama_ekosistem", "id_admin", "lokasi_geografis", "status_ekosistem"])
                    table.add_row(ekosistem_data)
                    print("Data yang akan diupdate:\n")
                    print(table)
                    nama_ekosistem = input("Masukkan nama ekosistem baru (biarkan kosong jika tidak ingin mengubah): ")
                    lokasi_geografis = input("Masukkan lokasi geografis baru (biarkan kosong jika tidak ingin mengubah): ")
                    status_ekosistem = input("Masukkan status ekosistem baru (biarkan kosong jika tidak ingin mengubah): ")
                    
                    update_query = "UPDATE ekosistem_darat SET "
                    update_values = []

                    if nama_ekosistem:
                        update_query += "nama_ekosistem = %s, "
                        update_values.append(nama_ekosistem)
                    if lokasi_geografis:
                        update_query += "lokasi_geografis = %s, "
                        update_values.append(lokasi_geografis)
                    if status_ekosistem:
                        update_query += "status_ekosistem = %s, "
                        update_values.append(status_ekosistem)

                    update_query += "id_admin = %s "
                    update_values.append(id_admin)

                    update_query += "WHERE id_ekosistem = %s"
                    update_values.append(id_ekosistem)

                    cursor.execute(update_query, update_values)

                    self.connection.commit()
                    print("|        --------------------------------------------------------       |")
                    print("|         Data Ekosistem Darat Berhasil Diperbarui Pada Database        |")
                    print("|        --------------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|                 Data Ekosistem Darat Tidak Ditemukan                |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                 Gagal Memperbarui Data Ekosistem Darat              |")
                print("|         -----------------------------------------------------       |")
                input("Tekan Enter untuk kembali ke menu admin...")
                self.menu(id_admin)
            finally:
                cursor.close()
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def delete(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                id_ekosistem = input("Masukkan ID ekosistem darat yang ingin dihapus: ")
                select_query = "SELECT * FROM ekosistem_darat WHERE id_ekosistem = %s"
                cursor.execute(select_query, (id_ekosistem,))
                ekosistem_data = cursor.fetchall()
                if ekosistem_data:
                    table = prettytable.PrettyTable(["id_ekosistem", "nama_ekosistem", "id_admin", "lokasi_geografis", "status_ekosistem"])
                    for row in ekosistem_data:
                        table.add_row(row)
                    print("Data yang akan dihapus:\n")
                    print(table)
                    confirm = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
                    if confirm.lower() == "y":
                        delete_query = "DELETE FROM ekosistem_darat WHERE id_ekosistem = %s"
                        cursor.execute(delete_query, (id_ekosistem,))
                        self.connection.commit()
                        print("Data berhasil dihapus dari tabel ekosistem darat.")
                        # Hapus data dari linked list
                        current = self.ekosistem_list.head
                        while current:
                            if current.data[0] == int(id_ekosistem):
                                if current.prev:
                                    current.prev.next = current.next
                                else:
                                    self.ekosistem_list.head = current.next
                                if current.next:
                                    current.next.prev = current.prev
                                else:
                                    self.ekosistem_list.tail = current.prev
                                break
                            current = current.next
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                    else:
                        print("|         -----------------------------------------------------       |")
                        print("|              Penghapusan Data Ekosistem Darat Dibatalkan            |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|                 Tidak Ditemukan Data Ekosistem Darat                |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                 Gagal Menghapus Data Ekosistem Darat                |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def menu(self, id_admin):
        print('''
==================================================
‖                MENU EKOSISTEM DARAT            ‖
==================================================''')
        print("| 1. Create                                      |")
        print("| 2. Read                                        |")
        print("| 3. Update                                      |")
        print("| 4. Delete                                      |")
        print("| 5. Sort                                        |")
        print("| 6. Search                                      |")
        print("| 7. Kembali                                     |")
        print("==================================================")
        try:
            choice = input("Pilih menu: ")

            if choice == "1":
                self.create(id_admin)
            elif choice == "2":
                self.read(id_admin)
            elif choice == "3":
                self.update(id_admin)
            elif choice == "4":
                self.delete(id_admin)
            elif choice == "5":
                order = input("Masukkan urutan (asc/desc): ")
                sorted_list_head = self.merge_sort(self.ekosistem_list.head, order)
                if sorted_list_head:
                    current = sorted_list_head
                    table = prettytable.PrettyTable(["id_ekosistem", "nama_ekosistem", "id_admin", "lokasi_geografis", "status_ekosistem"])
                    table._max_width = {"id_ekosistem": 3, "nama_ekosistem": 30, "id_admin": 3, "lokasi_geografis": 40, "status_ekosistem": 20}
                    while current:
                        table.add_row(current.data)
                        current = current.next
                    print("Data yang sudah diurutkan:")
                    print(table)
                else:
                    print("Data kosong.")  # Tambahan untuk menangani linked list kosong
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            elif choice == "6":
                self.search(id_admin)
            elif choice == "7":
                clear()
                menu_admin(id_admin)
            else:
                clear()
                self.menu(id_admin)
        except:
            input("\nTekan enter untuk melanjutkan....")
            clear()
            self.menu(id_admin)


class spesies_hewan:
    def __init__(self):
        self.connection = conn()
        self.hewan_list = DoubleLinkedList()

    def get_mid(self, head):
        if head is None:
            return None
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge_sort(self, head, order='asc'):
        if head is None or head.next is None:
            return head
        
        middle = self.get_mid(head)
        next_to_middle = middle.next
        
        middle.next = None
        
        left = self.merge_sort(head, order)
        right = self.merge_sort(next_to_middle, order)
        
        sorted_list = self.merge(left, right, order)
        return sorted_list

    def merge(self, left, right, order='asc'):
        result = None
        
        if left is None:
            return right
        if right is None:
            return left
        
        if order == 'asc':
            if left.data[0] <= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        elif order == 'desc':
            if left.data[0] >= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        
        return result

    def search(self, id_admin):
        if not self.connection:
            input("Tidak dapat terhubung ke database.")
            self.menu(id_admin)

        try:
            cursor = self.connection.cursor()
            target = input("Masukkan nama hewan yang ingin dicari: ")
            query = "SELECT * FROM spesies_hewan WHERE nama_hewan LIKE %s"
            cursor.execute(query, ("%" + target + "%",))
            results = cursor.fetchall()
            if results:
                table = prettytable.PrettyTable(["id_hewan", "nama_hewan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                for result in results:
                    table.add_row(result)
                print("Data ditemukan:")
                print(table)
            else:
                input("~~~~~DATA TIDAK DITEMUKAN!!!!!~~~~~.")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        except:
            
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        finally:
            if cursor:
                cursor.close()

    def create(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                nama_hewan = input("\nMasukkan nama hewan: ")
                id_ekosistem = input("Masukkan ID ekosistem: ")
                status_populasi = input("Masukkan status populasi: ")
                status_perlindungan = input("Masukkan status perlindungan: ")

                query = "INSERT INTO spesies_hewan(nama_hewan, id_ekosistem, status_populasi, status_perlindungan) VALUES (%s, %s, %s, %s)"
                data = (nama_hewan, id_ekosistem, status_populasi, status_perlindungan)
                cursor.execute(query, data)

                self.connection.commit()
                print("Data berhasil dimasukkan ke database spesies hewan.")
                # Menambah data ke dalam linked list
                self.hewan_list.append((cursor.lastrowid, nama_hewan, id_ekosistem, status_populasi, status_perlindungan))
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|             Gagal Memasukan Data ke Database Spesies Hewan          |")
                print("|         -----------------------------------------------------       |")
                input("Tekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)


    def read(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM spesies_hewan"
                cursor.execute(query)
                spesies_hewan = cursor.fetchall()
                if spesies_hewan:
                    table = prettytable.PrettyTable(["id_hewan", "nama_hewan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                    for hewan in spesies_hewan:
                        table.add_row(hewan)
                        # Menambah data ke dalam linked list
                        self.hewan_list.append(hewan)
                    print(table)
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|                     Data Spesies Hewan Tidak Tersedia               |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                cursor.close()
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                     Data Spesies Hewan Gagal Dibaca                 |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def read_by_user(self, id_user):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM spesies_hewan"
                cursor.execute(query)
                spesies_hewan = cursor.fetchall()
                if spesies_hewan:
                    table = prettytable.PrettyTable(["id_hewan", "nama_hewan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                    for hewan in spesies_hewan:
                        table.add_row(hewan)
                        # Menambah data ke dalam linked list
                        self.hewan_list.append(hewan)
                    print(table)
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    menu_user(id_user)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|                     Data Spesies Hewan Tidak Tersedia              |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    menu_user(id_user)
                cursor.close()
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                     Data Spesies Hewan Gagal Dibaca                 |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                menu_user(id_user)
            finally:
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu user...")
            clear()
            menu_user(id_user)

    def update(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                id_hewan = input("Masukkan ID hewan yang akan diupdate: ")
                select_query = "SELECT * FROM spesies_hewan WHERE id_hewan = %s"
                cursor.execute(select_query, (id_hewan,))
                hewan_data = cursor.fetchone()
                if hewan_data:
                    table = prettytable.PrettyTable(["id_hewan", "nama_hewan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                    table.add_row(hewan_data)
                    print("Data yang akan diupdate:\n")
                    print(table)
                    nama_hewan = input("Masukkan nama hewan baru (biarkan kosong jika tidak ingin mengubah): ")
                    id_ekosistem = input("Masukkan ID ekosistem baru (biarkan kosong jika tidak ingin mengubah): ")
                    status_populasi = input("Masukkan status populasi baru (biarkan kosong jika tidak ingin mengubah): ")
                    status_perlindungan = input("Masukkan status perlindungan baru (biarkan kosong jika tidak ingin mengubah): ")
                    
                    update_query = "UPDATE spesies_hewan SET "
                    update_values = []

                    if nama_hewan:
                        update_query += "nama_hewan = %s, "
                        update_values.append(nama_hewan)
                    if id_ekosistem:
                        update_query += "id_ekosistem = %s, "
                        update_values.append(id_ekosistem)
                    if status_populasi:
                        update_query += "status_populasi = %s, "
                        update_values.append(status_populasi)
                    if status_perlindungan:
                        update_query += "status_perlindungan = %s, "
                        update_values.append(status_perlindungan)

                    # Hapus koma terakhir dari kueri UPDATE
                    update_query = update_query.rstrip(', ')

                    # Tambahkan klausa WHERE
                    update_query += " WHERE id_hewan = %s"
                    update_values.append(id_hewan)

                    cursor.execute(update_query, update_values)

                    self.connection.commit()
                    print("|        --------------------------------------------------------       |")
                    print("|          Data Spesies Hewan Berhasil Diperbarui Pada Database         |")
                    print("|        --------------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|            Spesies Hewan Dengan ID Tersebut Tidak Ditemukan         |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                Gagal Memperbarui Data Spesies Hewan                 |")
                print("|         -----------------------------------------------------       |")
                input("Tekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)

            finally:
                cursor.close()
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def delete(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                id_spesies = input("Masukkan ID spesies hewan yang ingin dihapus: ")
                select_query = "SELECT * FROM spesies_hewan WHERE id_hewan = %s"
                cursor.execute(select_query, (id_spesies,))
                spesies_data = cursor.fetchall()
                if spesies_data:
                    table = prettytable.PrettyTable(["id_hewan", "nama_hewan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                    for row in spesies_data:
                        table.add_row(row)
                    print("Data yang akan dihapus:\n")
                    print(table)
                    confirm = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
                    if confirm.lower() == "y":
                        delete_query = "DELETE FROM spesies_hewan WHERE id_hewan = %s"
                        cursor.execute(delete_query, (id_spesies,))
                        self.connection.commit()
                        print("Data berhasil dihapus dari tabel spesies hewan.")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                    else:
                        print("|         -----------------------------------------------------       |")
                        print("|               Penghapusan Data Spesies Hewan Dibatalkan             |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|            Tidak Ditemukan Spesies Hewan Dengan ID Tersebut         |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                   Gagal Menghapus Data Spesies Hewan                |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)


    def menu(self, id_admin):
        print('''
==================================================
‖               MENU SPESIES HEWAN               ‖
==================================================''')
        print("| 1. Create                                      |")
        print("| 2. Read                                        |")
        print("| 3. Update                                      |")
        print("| 4. Delete                                      |")
        print("| 5. Sort                                        |")
        print("| 6. Search                                      |")
        print("| 7. Kembali                                     |")
        print("==================================================")
        try:
            choice = input("Pilih menu: ")

            if choice == "1":
                self.create(id_admin)
            elif choice == "2":
                self.read(id_admin)
            elif choice == "3":
                self.update(id_admin)
            elif choice == "4":
                self.delete(id_admin)
            elif choice == "5":
                order = input("Masukkan urutan (asc/desc): ")
                sorted_list_head = self.merge_sort(self.hewan_list.head, order)
                if sorted_list_head:
                    current = sorted_list_head
                    table = prettytable.PrettyTable(["id_hewan", "nama_hewan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                    while current:
                        table.add_row(current.data)
                        current = current.next
                    print("Data yang sudah diurutkan:")
                    print(table)
                else:
                    print("~~~~~DATA KOSONG!!!!~~~~~")  # Tambahan untuk menangani linked list kosong
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            elif choice == "6":
                self.search(id_admin)
            elif choice == "7":
                clear()
                menu_admin(id_admin)
            else:
                clear()
                self.menu(id_admin)
        except:
            input("\nTekan enter untuk melanjutkan....")
            clear()
            self.menu(id_admin)


class spesies_tumbuhan:
    def __init__(self):
        self.connection = conn()
        self.tumbuhan_list = DoubleLinkedList()

    def get_mid(self, head):
        if head is None:
            return None
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge_sort(self, head, order='asc'):
        if head is None or head.next is None:
            return head
        
        middle = self.get_mid(head)
        next_to_middle = middle.next
        
        middle.next = None
        
        left = self.merge_sort(head, order)
        right = self.merge_sort(next_to_middle, order)
        
        sorted_list = self.merge(left, right, order)
        return sorted_list

    def merge(self, left, right, order='asc'):
        result = None
        
        if left is None:
            return right
        if right is None:
            return left


        if order == 'asc':
            if left.data[0] <= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        elif order == 'desc':
            if left.data[0] >= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        
        return result

    def search(self, id_admin):
        if not self.connection:
            input("Tidak dapat terhubung ke database.")
            self.menu(id_admin)

        try:
            cursor = self.connection.cursor()
            target = input("Masukkan nama tumbuhan yang ingin dicari: ")
            query = "SELECT * FROM spesies_tumbuhan WHERE nama_tumbuhan LIKE %s"
            cursor.execute(query, ("%" + target + "%",))
            results = cursor.fetchall()
            if results:
                table = prettytable.PrettyTable(["id_tumbuhan", "nama_tumbuhan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                for result in results:
                    table.add_row(result)
                print("Data ditemukan:")
                print(table)
            else:
                input("~~~~~DATA TIDAK DITEMUKAN!!!!!~~~~~.")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        except:
            
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        finally:
            if cursor:
                cursor.close()

    def create(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                nama_tumbuhan = input("\nMasukkan nama tumbuhan: ")
                id_ekosistem = input("Masukkan ID ekosistem: ")
                status_populasi = input("Masukkan status populasi: ")
                status_perlindungan = input("Masukkan status perlindungan: ")

                query = "INSERT INTO spesies_tumbuhan(nama_tumbuhan, id_ekosistem, status_populasi, status_perlindungan) VALUES (%s, %s, %s, %s)"
                data = (nama_tumbuhan, id_ekosistem, status_populasi, status_perlindungan)
                cursor.execute(query, data)

                self.connection.commit()
                print("Data berhasil dimasukkan ke database spesies tumbuhan.")
                # Menambah data ke dalam linked list
                self.tumbuhan_list.append((cursor.lastrowid, nama_tumbuhan, id_ekosistem, status_populasi, status_perlindungan))
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                Gagal Masuk ke Database Spesies Tumbuhan             |")
                print("|         -----------------------------------------------------       |")
                input("Tekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def read(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM spesies_tumbuhan"
                cursor.execute(query)
                spesies_tumbuhan = cursor.fetchall()
                if spesies_tumbuhan:
                    table = prettytable.PrettyTable(["id_tumbuhan", "nama_tumbuhan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                    for tumbuhan in spesies_tumbuhan:
                        table.add_row(tumbuhan)
                        # Menambah data ke dalam linked list
                        self.tumbuhan_list.append(tumbuhan)
                    print(table)
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|                   Data Spesies Tumbuhan Tidak Tersedia              |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                cursor.close()
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                   Data Spesies Tumbuhan Gagal Dibaca                |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def read_by_user(self, id_user):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM spesies_tumbuhan"
                cursor.execute(query)
                spesies_tumbuhan = cursor.fetchall()
                if spesies_tumbuhan:
                    table = prettytable.PrettyTable(["id_tumbuhan", "nama_tumbuhan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                    for tumbuhan in spesies_tumbuhan:
                        table.add_row(tumbuhan)
                        # Menambah data ke dalam linked list
                        self.tumbuhan_list.append(tumbuhan)
                    print(table)
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    menu_user(id_user)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|                   Data Spesies Tumbuhan Tidak Tersedia              |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    menu_user(id_user)
                cursor.close()
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                   Data Spesies Tumbuhan Gagal Dibaca                |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                menu_user(id_user)
            finally:
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu user...")
            clear()
            menu_user(id_user)

    def update(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                id_tumbuhan = input("Masukkan ID tumbuhan yang akan diupdate: ")
                select_query = "SELECT * FROM spesies_tumbuhan WHERE id_tumbuhan = %s"
                cursor.execute(select_query, (id_tumbuhan,))
                tumbuhan_data = cursor.fetchone()
                if tumbuhan_data:
                    table = prettytable.PrettyTable(["id_tumbuhan", "nama_tumbuhan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                    table.add_row(tumbuhan_data)
                    print("Data yang akan diupdate:\n")
                    print(table)
                    nama_tumbuhan = input("Masukkan nama tumbuhan baru (biarkan kosong jika tidak ingin mengubah): ")
                    id_ekosistem = input("Masukkan ID ekosistem baru (biarkan kosong jika tidak ingin mengubah): ")
                    status_populasi = input("Masukkan status populasi baru (biarkan kosong jika tidak ingin mengubah): ")
                    status_perlindungan = input("Masukkan status perlindungan baru (biarkan kosong jika tidak ingin mengubah): ")
                    
                    update_query = "UPDATE spesies_tumbuhan SET "
                    update_values = []

                    if nama_tumbuhan:
                        update_query += "nama_tumbuhan = %s, "
                        update_values.append(nama_tumbuhan)
                    if id_ekosistem:
                        update_query += "id_ekosistem = %s, "
                        update_values.append(id_ekosistem)
                    if status_populasi:
                        update_query += "status_populasi = %s, "
                        update_values.append(status_populasi)
                    if status_perlindungan:
                        update_query += "status_perlindungan = %s, "
                        update_values.append(status_perlindungan)

                    update_query = update_query.rstrip(', ')

                    # Tambahkan klausa WHERE
                    update_query += " WHERE id_tumbuhan = %s"
                    update_values.append(id_tumbuhan)

                    cursor.execute(update_query, update_values)

                    self.connection.commit()
                    print("|        --------------------------------------------------------       |")
                    print("|        Data Spesies Tumbuhan Berhasil Diperbarui Pada Database        |")
                    print("|        --------------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|          Spesies Tumbuhan Dengan ID Tersebut Tidak Ditemukan        |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                 Gagal Memperbarui Data Spesies Tumbuhan             |")
                print("|         -----------------------------------------------------       |")
                input("Tekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
                self.connection.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def delete(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                id_tumbuhan = input("Masukkan ID tumbuhan yang ingin dihapus: ")
                select_query = "SELECT * FROM spesies_tumbuhan WHERE id_tumbuhan = %s"
                cursor.execute(select_query, (id_tumbuhan,))
                tumbuhan_data = cursor.fetchall()
                if tumbuhan_data:
                    table = prettytable.PrettyTable(["id_tumbuhan", "nama_tumbuhan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                    for row in tumbuhan_data:
                        table.add_row(row)
                    print("Data yang akan dihapus:\n")
                    print(table)
                    confirm = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
                    if confirm.lower() == "y":
                        delete_query = "DELETE FROM spesies_tumbuhan WHERE id_tumbuhan = %s"
                        cursor.execute(delete_query, (id_tumbuhan,))
                        self.connection.commit()
                        print("|         -----------------------------------------------------       |")
                        print("|                         Data Berhasil Dihapus                       |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                    else:
                        print("|         -----------------------------------------------------       |")
                        print("|                       Penghapusan Data Dibatalkan                   |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|          Spesies Tumbuhan Dengan ID Tersebut Tidak Ditemukan        |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except:
                
                print("|         -----------------------------------------------------       |")
                print("|                 Gagal Menghapus Data Spesies Tumbuhan               |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
                self.connection.close()
        else:
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def menu(self, id_admin):
        print('''
==================================================
‖             MENU SPESIES TUMBUHAN              ‖
==================================================''')
        print("| 1. Create                                      |")
        print("| 2. Read                                        |")
        print("| 3. Update                                      |")
        print("| 4. Delete                                      |")
        print("| 5. Sort                                        |")
        print("| 6. Search                                      |")
        print("| 7. Kembali                                     |")
        print("==================================================")
        choice = input("Pilih menu: ")
        try:
            if choice == "1":
                self.create(id_admin)
            elif choice == "2":
                self.read(id_admin)
            elif choice == "3":
                self.update(id_admin)
            elif choice == "4":
                self.delete(id_admin)
            elif choice == "5":
                order = input("Masukkan urutan (asc/desc): ")
                sorted_list_head = self.merge_sort(self.tumbuhan_list.head, order)
                if sorted_list_head:
                    current = sorted_list_head
                    table = prettytable.PrettyTable(["id_tumbuhan", "nama_tumbuhan", "id_ekosistem", "status_populasi", "status_perlindungan"])
                    while current:
                        table.add_row(current.data)
                        current = current.next
                    print("Data yang sudah diurutkan:")
                    print(table)
                else:
                    print("~~~~~DATA KOSONG!!!!~~~~~")  # Tambahan untuk menangani linked list kosong
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            elif choice == "6":
                self.search(id_admin)
            elif choice == "7":
                clear()
                menu_admin(id_admin)
            else:
                clear()
                self.menu(id_admin)
        except:
            input("\nTekan enter untuk melanjutkan....")
            clear()
            self.menu(id_admin)



class laporan:
    def __init__(self):
        self.connection = conn()
        self.laporan_list = DoubleLinkedList()

    def get_mid(self, head):
        if head is None:
            return None
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge_sort(self, head, order='asc'):
        if head is None or head.next is None:
            return head
        
        middle = self.get_mid(head)
        next_to_middle = middle.next
        
        middle.next = None
        
        left = self.merge_sort(head, order)
        right = self.merge_sort(next_to_middle, order)
        
        sorted_list = self.merge(left, right, order)
        return sorted_list

    def merge(self, left, right, order='asc'):
        result = None
        
        if left is None:
            return right
        if right is None:
            return left


        if order == 'asc':
            if left.data[0] <= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        elif order == 'desc':
            if left.data[0] >= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        
        return result


    def search(self, id_admin):
        if not self.connection:
            input("Tidak dapat terhubung ke database.")
            self.menu(id_admin)

        try:
            cursor = self.connection.cursor()
            target = input("Masukkan isi laporan yang ingin dicari: ")
            query = "SELECT * FROM laporan WHERE isi_laporan LIKE %s"
            cursor.execute(query, ("%" + target + "%",))
            results = cursor.fetchall()
            if results:
                table = prettytable.PrettyTable(["id_laporan", "isi_laporan", "id_user", "id_admin"])
                for result in results:
                    table.add_row(result)
                print("Data ditemukan:")
                print(table)
            else:
                input("~~~~~DATA TIDAK DITEMUKAN!!!!!~~~~~.")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        except:
            
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        finally:
            if cursor:
                cursor.close()

    def create(self, id_user):
            clear()
            print('''
==================================================
‖                  MEMBUAT LAPORAN               ‖
==================================================''')
            isi_laporan = input("Masukkan isi laporan Anda: ")

            # Mendapatkan id admin secara random dari database
            if self.connection:
                try:
                    cursor = self.connection.cursor()
                    query_get_admin_ids = "SELECT id_admin FROM admin"
                    cursor.execute(query_get_admin_ids)
                    admin_ids = cursor.fetchall()
                    if admin_ids:
                        random_admin_id = random.choice(admin_ids)[0]

                        # Menyimpan laporan ke database
                        query_insert_laporan = "INSERT INTO laporan (isi_laporan, id_user, id_admin) VALUES (%s, %s, %s)"
                        cursor.execute(query_insert_laporan, (isi_laporan, id_user, random_admin_id))
                        self.connection.commit()
                        print("Laporan berhasil dibuat, berikut isi laporannya.")
                        print("Isi laporan:", isi_laporan)
                        print("ID User:", id_user)
                        print("ID Admin:", random_admin_id)

                        print("|     -------------------------------------------------------------------       |")
                        print("|                               PERINGATAN!!!                                   |")
                        print("|     -------------------------------------------------------------------       |")
                        print("|      Jika laporan anda tidak valid, admin dapat menghapus laporan anda        |")
                        print("|     -------------------------------------------------------------------       |")
                        input("Tekan Enter untuk kembali ke menu user...")
                        clear()
                        menu_user(id_user)
                    else:
                        clear()
                        print("|         -----------------------------------------------------       |")
                        print("|          Tidak Ada Admin Yang Tersedia Untuk Membuat Laporan        |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk melanjutkan...")
                        clear()
                        menu_user(id_user)
                except:
                    clear()
                    print("|         -----------------------------------------------------       |")
                    print("|                           Gagal Membuat Laporan                     |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk melanjutkan...")
                    clear()
                    menu_user(id_user)
                finally:
                    cursor.close()
                    self.connection.close()
            else:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                   Tidak Dapat Terhubung Ke Database                 |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan enter untuk melanjutkan...")
                clear()
                menu_user(id_user)

    def read(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM laporan"
                cursor.execute(query)
                laporan = cursor.fetchall()
                if laporan:  
                    table = prettytable.PrettyTable(["id_laporan", "isi_laporan", "id_user", "id_admin"])
                    table._max_width = {"id_laporan": 3, "isi_laporan": 50, "id_user": 3, "id_admin": 3}
                    for data in laporan:  
                        table.add_row(data)
                        self.laporan_list.append(data)  # Menambahkan data ke dalam linked list
                    print(table)
                    input("Tekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                else:
                    clear()
                    print("|         -----------------------------------------------------       |")
                    print("|                     Data Laporan Tidak Tersedia                     |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                       Data Laporan Gagal Dibaca                     |")
                print("|         -----------------------------------------------------       |")
                clear()
                input("\nTekan Enter untuk kembali ke menu admin...")
                self.menu(id_admin)
            finally:
                cursor.close()
                self.connection.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)


    def update(self, id_admin):
            if self.connection:
                try:
                    cursor = self.connection.cursor()
                    
                    # Input data yang akan diupdate dari pengguna
                    id_laporan = input("Masukkan ID laporan yang akan diupdate: ")
                    
                    # Query SELECT untuk mendapatkan data spesifik berdasarkan id_laporan
                    select_query = "SELECT * FROM laporan WHERE id_laporan = %s"
                    cursor.execute(select_query, (id_laporan,))
                    laporan_data = cursor.fetchone()
                    
                    # Menampilkan data yang akan diupdate menggunakan PrettyTable
                    if laporan_data:
                        table = prettytable.PrettyTable(["id_laporan", "isi_laporan", "id_user", "id_admin"])
                        table.add_row(laporan_data)
                        print("Data yang akan diupdate:\n")
                        print(table)
                        
                        # Meminta input data baru dari pengguna
                        isi_laporan = input("Masukkan isi laporan baru (biarkan kosong jika tidak ingin mengubah): ")
                        
                        # Query UPDATE untuk memperbarui data di tabel laporan
                        update_query = "UPDATE laporan SET "
                        update_values = []

                        # Membuat daftar nilai yang akan diubah
                        if isi_laporan:
                            update_query += "isi_laporan = %s, "
                            update_values.append(isi_laporan)

                        # Menambahkan id_admin yang sedang mengedit sekarang
                        update_query += "id_admin = %s "
                        update_values.append(id_admin)

                        # Menambahkan klausa WHERE
                        update_query += "WHERE id_laporan = %s"
                        update_values.append(id_laporan)

                        # Menjalankan query UPDATE dengan nilai yang diperbarui
                        cursor.execute(update_query, update_values)

                        self.connection.commit()
                        print("|         -----------------------------------------------------       |")
                        print("|             Data Laporan Berhasil Diperbarui Pada Database          |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                    else:
                        clear()
                        print("|         -----------------------------------------------------       |")
                        print("|               Laporan Dengan ID Tersebut Tidak Ditemukan            |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)

                except:
                    clear()
                    print("|         -----------------------------------------------------       |")
                    print("|                    Gagal Memperbarui Data Laporan                   |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)

                finally:
                    cursor.close()
                    self.connection.close()
            else:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                   Tidak Dapat Terhubung Ke Database                 |")
                print("|         -----------------------------------------------------       |")
                clear()
                self.menu(id_admin)

    def delete(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                
                # Meminta input id_laporan dari pengguna
                id_laporan = input("Masukkan ID laporan yang ingin dihapus: ")
                
                # Query SELECT untuk menampilkan data spesifik sebelum penghapusan
                select_query = "SELECT * FROM laporan WHERE id_laporan = %s"
                cursor.execute(select_query, (id_laporan,))
                laporan_data = cursor.fetchall()
                
                # Menampilkan data yang akan dihapus menggunakan PrettyTable
                if laporan_data:
                    table = prettytable.PrettyTable(["id_laporan", "isi_laporan", "id_user", "id_admin"])
                    for row in laporan_data:
                        table.add_row(row)
                    print("Data yang akan dihapus:\n")
                    print(table)
                    
                    # Konfirmasi pengguna untuk menghapus data
                    confirm = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
                    if confirm.lower() == "y":
                        # Query DELETE untuk menghapus data dari tabel laporan
                        delete_query = "DELETE FROM laporan WHERE id_laporan = %s"
                        cursor.execute(delete_query, (id_laporan,))
                        self.connection.commit()
                        print("|         -----------------------------------------------------       |")
                        print("|                           Data Berhasil Di Hapus                    |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan enter untuk melanjutkan....")
                        clear()
                        self.menu(id_admin)
                    else:
                        clear()
                        print("|         -----------------------------------------------------       |")
                        print("|                             Data Gagal Di Hapus                     |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan enter untuk melanjutkan....")
                        clear()
                        self.menu(id_admin)
                else:
                    clear()
                    print("|         -----------------------------------------------------       |")
                    print("|             Data Laporan Dengan ID Tersebut Tidak Ditemukan         |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan enter untuk melanjutkan....")
                    self.menu(id_admin)

            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                      Gagal Menghapus Data Laporan                   |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan enter untuk melanjutkan....")
                clear()
                self.menu(id_admin)

            finally:
                cursor.close()
                self.connection.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan enter untuk melanjutkan....")
            clear()
            menu_admin(id_admin)

    def menu(self, id_admin):
        print('''
==================================================
‖                    MENU LAPORAN                ‖
==================================================''')
        print("| 1. Baca Laporan                               |")
        print("| 2. Update Laporan                             |")
        print("| 3. Hapus Laporan                              |")
        print("| 4. Sort Laporan                               |")
        print("| 5. Search Laporan                             |")
        print("| 6. Kembali ke menu sebelumnya                 |")
        print("==================================================")

        try:
            choice = input("Pilih menu: ")

            if choice == "1":
                self.read(id_admin)
            elif choice == "2":
                self.update(id_admin)
            elif choice == "3":
                self.delete(id_admin)
            elif choice == "4":
                order = input("Masukkan urutan (asc/desc): ")
                sorted_list_head = self.merge_sort(self.laporan_list.head, order)
                if sorted_list_head:
                    current = sorted_list_head
                    table = prettytable.PrettyTable(["id_laporan", "isi_laporan", "id_user", "id_admin"])
                    table._max_width = {"id_laporan": 3, "isi_laporan": 50, "id_user": 3, "id_admin": 3}
                    while current:
                        table.add_row(current.data)
                        current = current.next
                    print("Data yang sudah diurutkan:")
                    print(table)
                else:
                    print("~~~~~DATA KOSONG!!!!~~~~~")  # Tambahan untuk menangani linked list kosong
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            elif choice == "5":
                self.search(id_admin)
            elif choice == "6":
                clear()
                menu_admin(id_admin)
            else:
                clear()
                self.menu(id_admin)
        except:
            input("\nTekan enter untuk melanjutkan....")
            clear()
            self.menu(id_admin)



class user:
    def __init__(self):
        self.connection = conn()
        self.user_list = DoubleLinkedList()

    def get_mid(self, head):
        if head is None:
            return None
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge_sort(self, head, order='asc'):
        if head is None or head.next is None:
            return head
        
        middle = self.get_mid(head)
        next_to_middle = middle.next
        
        middle.next = None
        
        left = self.merge_sort(head, order)
        right = self.merge_sort(next_to_middle, order)
        
        sorted_list = self.merge(left, right, order)
        return sorted_list

    def merge(self, left, right, order='asc'):
        result = None
        
        if left is None:
            return right
        if right is None:
            return left


        if order == 'asc':
            if left.data[0] <= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        elif order == 'desc':
            if left.data[0] >= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        
        return result


    def search(self, id_admin):
        if not self.connection:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("Tekan enter untuk melanjutkan....")
            self.menu(id_admin)

        try:
            cursor = self.connection.cursor()
            target = input("Masukkan user yang ingin dicari: ")
            query = "SELECT * FROM user WHERE nama_user LIKE %s"
            cursor.execute(query, ("%" + target + "%",))
            results = cursor.fetchall()
            if results:
                table = prettytable.PrettyTable(["id_user", "nama_user", "password", "no_telpon"])
                for result in results:
                    table.add_row(result)
                print("Data ditemukan:")
                print(table)
            else:
                input("~~~~~DATA TIDAK DITEMUKAN!!!!!~~~~~.")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        except:
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        finally:
            if cursor:
                cursor.close()

    def create_by_admin(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                nama_user = input("\nMasukkan nama user: ")
                password = input("Masukkan password: ")
                no_telpon = input("Masukkan nomor telepon: ")

                # Tambahkan data user ke database
                query = "INSERT INTO user(nama_user, password, no_telpon) VALUES (%s, %s, %s)"
                data = (nama_user, password, no_telpon)
                cursor.execute(query, data)

                self.connection.commit()
                print("|         -----------------------------------------------------       |")
                print("|                     Data User Berhasil Ditambahkan                  |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
                # Tambahkan data ke dalam linked list
                self.user_list.append((cursor.lastrowid, nama_user, password, no_telpon))
            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                        Gagal Menemukan Data User                    |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu user...")
            clear()
            self.menu(id_admin)

    def read(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM user"
                cursor.execute(query)
                users = cursor.fetchall()
                if users:
                    table = prettytable.PrettyTable(["id_user", "nama_user", "password", "no_telpon"])
                    for user in users:
                        table.add_row(user)
                        # Menambah data pengguna ke dalam linked list
                        self.user_list.append(user)  # Perubahan disini
                    print("Data pengguna:")
                    print(table)
                else:
                    clear()
                    print("|         -----------------------------------------------------       |")
                    print("|                           Tidak ada data pengguna                   |")
                    print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
                cursor.close()
            except:
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                self.connection.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)



    def update(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                id_user_to_update = input("Masukkan ID user yang akan diupdate: ")
                select_query = "SELECT * FROM user WHERE id_user = %s"
                cursor.execute(select_query, (id_user_to_update,))
                user_data = cursor.fetchone()
                if user_data:
                    table = prettytable.PrettyTable(["id_user", "nama_user", "password", "no_telpon"])
                    table.add_row(user_data)
                    print("Data user yang akan diupdate:\n")
                    print(table)
                    nama_user = input("Masukkan nama user baru (biarkan kosong jika tidak ingin mengubah): ")
                    password = input("Masukkan password baru (biarkan kosong jika tidak ingin mengubah): ")
                    no_telpon = input("Masukkan nomor telepon baru (biarkan kosong jika tidak ingin mengubah): ")
                    
                    update_query = "UPDATE user SET "
                    update_values = []

                    if nama_user:
                        update_query += "nama_user = %s, "
                        update_values.append(nama_user)
                    if password:
                        update_query += "password = %s, "
                        update_values.append(password)
                    if no_telpon:
                        update_query += "no_telpon = %s, "
                        update_values.append(no_telpon)

                    # Menghapus koma terakhir dan menambahkan klausa WHERE
                    update_query = update_query[:-2] + " WHERE id_user = %s"
                    update_values.append(id_user_to_update)

                    cursor.execute(update_query, update_values)

                    self.connection.commit()
                    print("|         -----------------------------------------------------       |")
                    print("|                     Data User Berhasil Diperbarui                   |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    self.menu(id_admin)
                else:
                    clear()
                    print("|         -----------------------------------------------------       |")
                    print("|               User Dengan ID Tersebut Tidak Ditemukan               |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    self.menu(id_admin)
            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                       Data User Gagal Diperbarui                    |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu user...")
            clear()
            self.menu(id_admin)

    def delete(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                id_user_to_delete = input("Masukkan ID user yang ingin dihapus: ")
                select_query = "SELECT * FROM user WHERE id_user = %s"
                cursor.execute(select_query, (id_user_to_delete,))
                user_data = cursor.fetchall()
                if user_data:
                    table = prettytable.PrettyTable(["id_user", "nama_user", "password", "no_telpon"])
                    for user_row in user_data:
                        table.add_row(user_row)
                    print("Data user yang akan dihapus:\n")
                    print(table)
                    confirm = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
                    if confirm.lower() == "y":
                        delete_query = "DELETE FROM user WHERE id_user = %s"
                        cursor.execute(delete_query, (id_user_to_delete,))
                        self.connection.commit()
                        print("|         -----------------------------------------------------       |")
                        print("|                      Data User Berhasil Dihapus                     |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu user...")
                        clear()
                        self.menu(id_admin)
                    else:
                        clear()
                        print("|         -----------------------------------------------------       |")
                        print("|                   Penghapusan Data User Dibatalkan                  |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu user...")
                        clear()
                        self.menu(id_admin)
                else:
                    clear()
                    print("|         -----------------------------------------------------       |")
                    print("|             Tidak ditemukan data user dengan ID tersebut            |")
                    print("|         -----------------------------------------------------       |")
            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                         Data User Gagal Dihapus                     |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu user...")
            clear()
            self.menu(id_admin)

    def menu(self, id_admin):
        print('''
=====================================================
‖                  MENU ADMINISTRASI USER           ‖
=====================================================''')
        print("| 1. Create User                                    |")
        print("| 2. Read User                                      |")
        print("| 3. Update User                                    |")
        print("| 4. Delete User                                    |")
        print("| 5. Sort User                                      |")
        print("| 6. Search User                                    |")
        print("| 7. Kembali                                        |")
        print("=====================================================")

        try:
            choice = input("Pilih menu: ")

            if choice == "1":
                self.create_by_admin(id_admin)
            elif choice == "2":
                self.read(id_admin)
            elif choice == "3":
                self.update(id_admin)
            elif choice == "4":
                self.delete(id_admin)
            elif choice == "5":
                order = input("Masukkan urutan (asc/desc): ")
                sorted_list_head = self.merge_sort(self.user_list.head, order)
                if sorted_list_head:
                    current = sorted_list_head
                    table = prettytable.PrettyTable(["id_user", "nama_user", "password", "no_telpon"])
                    while current:
                        table.add_row(current.data)
                        current = current.next
                    print("Data yang sudah diurutkan:")
                    print(table)
                else:
                    print("~~~~~DATA KOSONG!!!!~~~~~")  # Tambahan untuk menangani linked list kosong
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            elif choice == "6":
                self.search(id_admin)
            elif choice == "7":
                clear()
                menu_admin(id_admin)
            else:
                clear()
                self.menu(id_admin)
        except:
            input("\nTekan enter untuk melanjutkan....")
            clear()
            self.menu(id_admin)



class admin:
    def __init__(self):
        self.connection = conn()
        self.admin_list = DoubleLinkedList()

    def get_mid(self, head):
        if head is None:
            return None
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def merge_sort(self, head, order='asc'):
        if head is None or head.next is None:
            return head
        
        middle = self.get_mid(head)
        next_to_middle = middle.next
        
        middle.next = None
        
        left = self.merge_sort(head, order)
        right = self.merge_sort(next_to_middle, order)
        
        sorted_list = self.merge(left, right, order)
        return sorted_list

    def merge(self, left, right, order='asc'):
        result = None
        
        if left is None:
            return right
        if right is None:
            return left


        if order == 'asc':
            if left.data[0] <= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        elif order == 'desc':
            if left.data[0] >= right.data[0]:
                result = left
                result.next = self.merge(left.next, right, order)
            else:
                result = right
                result.next = self.merge(left, right.next, order)
        
        return result


    def search(self, id_admin):
        if not self.connection:
            input("Tidak dapat terhubung ke database.....")
            self.menu(id_admin)

        try:
            cursor = self.connection.cursor()
            target = input("Masukkan admin yang ingin dicari: ")
            query = "SELECT * FROM admin WHERE nama_admin LIKE %s"
            cursor.execute(query, ("%" + target + "%",))
            results = cursor.fetchall()
            if results:
                table = prettytable.PrettyTable(["id_admin", "nama_admin", "password", "no_telpon"])
                for result in results:
                    table.add_row(result)
                print("Data ditemukan:")
                print(table)
            else:
                input("~~~~~DATA TIDAK DITEMUKAN!!!!!~~~~~.")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        except:
            
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        finally:
            if cursor:
                cursor.close()

    def create(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                nama_admin = input("\nMasukkan nama admin: ")
                password = input("Masukkan password: ")
                no_telpon = input("Masukkan nomor telepon: ")

                # Tambahkan data admin ke database
                query = "INSERT INTO admin(nama_admin, password, no_telpon) VALUES (%s, %s, %s)"
                data = (nama_admin, password, no_telpon)
                cursor.execute(query, data)

                self.connection.commit()
                print("|         -----------------------------------------------------       |")
                print("|                Data Admin Berhasil Dimasukkan Database              |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
                # Tambahkan data ke dalam linked list
                self.admin_list.append((cursor.lastrowid, nama_admin, password, no_telpon))
            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                      Data Admin Gagal Dimasukkan                    |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def read(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                query = "SELECT * FROM admin"
                cursor.execute(query)
                admin_data = cursor.fetchall()
                if admin_data:
                    table = prettytable.PrettyTable(["id_admin", "nama_admin", "password", "no_telpon"])
                    for admin_row in admin_data:
                        table.add_row(admin_row)
                        self.admin_list.append(admin_row)  # Menambahkan data ke dalam linked list
                    print(table)
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                else:
                    clear()
                    print("|         -----------------------------------------------------       |")
                    print("|                       Data Admin Tidak Tersedia                     |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                        Data Admin Gagal Dibaca                      |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)


    def update(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                id_admin_to_update = input("Masukkan ID admin yang akan diupdate: ")
                select_query = "SELECT * FROM admin WHERE id_admin = %s"
                cursor.execute(select_query, (id_admin_to_update,))
                admin_data = cursor.fetchone()
                if admin_data:
                    table = prettytable.PrettyTable(["id_admin", "nama_admin", "password", "no_telpon"])
                    table.add_row(admin_data)
                    print("Data admin yang akan diupdate:\n")
                    print(table)
                    nama_admin = input("Masukkan nama admin baru (biarkan kosong jika tidak ingin mengubah): ")
                    password = input("Masukkan password baru (biarkan kosong jika tidak ingin mengubah): ")
                    no_telpon = input("Masukkan nomor telepon baru (biarkan kosong jika tidak ingin mengubah): ")
                    
                    update_query = "UPDATE admin SET "
                    update_values = []

                    if nama_admin:
                        update_query += "nama_admin = %s, "
                        update_values.append(nama_admin)
                    if password:
                        update_query += "password = %s, "
                        update_values.append(password)
                    if no_telpon:
                        update_query += "no_telpon = %s, "
                        update_values.append(no_telpon)

                    # Menghapus koma terakhir dan menambahkan klausa WHERE
                    update_query = update_query[:-2] + " WHERE id_admin = %s"
                    update_values.append(id_admin_to_update)

                    cursor.execute(update_query, update_values)

                    self.connection.commit()
                    print("|         -----------------------------------------------------       |")
                    print("|                    Data Admin Berhasil Diperbarui                   |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                else:
                    clear()
                    print("|         -----------------------------------------------------       |")
                    print("|               Admin Dengan ID Tersebut Tidak Ditemukan              |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                     Gagal Memperbarui Data Admin                    |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def delete(self, id_admin):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                id_admin_to_delete = input("Masukkan ID admin yang ingin dihapus: ")
                select_query = "SELECT * FROM admin WHERE id_admin = %s"
                cursor.execute(select_query, (id_admin_to_delete,))
                admin_data = cursor.fetchall()
                if admin_data:
                    table = prettytable.PrettyTable(["id_admin", "nama_admin", "password", "no_telpon"])
                    for admin_row in admin_data:
                        table.add_row(admin_row)
                    print("Data admin yang akan dihapus:\n")
                    print(table)
                    confirm = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
                    if confirm.lower() == "y":
                        delete_query = "DELETE FROM admin WHERE id_admin = %s"
                        cursor.execute(delete_query, (id_admin_to_delete,))
                        self.connection.commit()
                        print("|         -----------------------------------------------------       |")
                        print("|                    Data Admin Berhasilih Dihapus                    |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                    else:
                        clear()
                        print("|         -----------------------------------------------------       |")
                        print("|                   Penghapusan Data Admin Dibatalkan                 |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                else:
                    clear()
                    print("|         -----------------------------------------------------       |")
                    print("|            Data Admin Dengan ID Tersebut Tidak Ditemukan            |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
            except:
                clear()
                print("|         -----------------------------------------------------       |")
                print("|                       Gagal Menghapus Data Admin                    |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def menu(self, id_admin):
        print('''
==========================================================
‖                   MENU ADMINISTRASI ADMIN              ‖
==========================================================''')
        print("| 1. Create Admin                                   |")
        print("| 2. Read Admin                                     |")
        print("| 3. Update Admin                                   |")
        print("| 4. Delete Admin                                   |")
        print("| 5. Sort Admin                                     |")
        print("| 6. Search Admin                                   |")
        print("| 7. Kembali                                        |")
        print("=====================================================")

        try:
            choice = input("Pilih menu: ")

            if choice == "1":
                self.create(id_admin)
            elif choice == "2":
                self.read(id_admin)
            elif choice == "3":
                self.update(id_admin)
            elif choice == "4":
                self.delete(id_admin)
            elif choice == "5":
                order = input("Masukkan urutan (asc/desc): ")
                sorted_list_head = self.merge_sort(self.admin_list.head, order)
                if sorted_list_head:
                    current = sorted_list_head
                    table = prettytable.PrettyTable(["id_admin", "nama_admin", "password", "no_telpon"])
                    while current:
                        table.add_row(current.data)
                        current = current.next
                    print("Data yang sudah diurutkan:")
                    print(table)
                else:
                    print("====================================")
                    print("|         DATA KOSONG!!!           |")  # Tambahan untuk menangani linked list kosong
                    print("====================================")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            elif choice == "6":
                self.search(id_admin)
            elif choice == "7":
                clear()
                menu_admin(id_admin)
            else:
                clear()
                self.menu(id_admin)
        except:
            clear()
            input("\nTekan enter untuk melanjutkan....")
            self.menu(id_admin)




#------------Admin------------#
def menu_admin(id_admin):
    try:
        print('''
==================================================
‖                     MENU ADMIN                 ‖
==================================================''')
        print("| 1. Ekosistem Darat                             |")
        print("| 2. Spesies Hewan                               |")
        print("| 3. Spesies Tumbuhan                            |")
        print("| 4. Laporan                                     |")
        print("| 5. User                                        |")
        print("| 6. Admin                                       |")
        print("| 7. Kembali ke Menu Sebelumnya                  |")
        print("==================================================")

        choice = input("Pilih menu: ")

        if choice == "1":
            clear()
            darat = EkosistemDarat()
            darat.menu(id_admin)
        elif choice == "2":
            clear()
            hewan = spesies_hewan()
            hewan.menu(id_admin)  # Pastikan objek hewan dibuat sebelum pemanggilan metode menu
        elif choice == "3":
            clear()
            tumbuhan = spesies_tumbuhan()
            tumbuhan.menu(id_admin)
        elif choice == "4":
            clear()
            lapor = laporan()
            lapor.menu(id_admin)
        elif choice == "5":
            clear()
            userr = user()
            userr.menu(id_admin)
        elif choice == "6":
            clear()
            adminn = admin()
            adminn.menu(id_admin)
        elif choice == "7":
            clear()
            print("\t\t\t Keluar dari Menu Admin.....")
            time.sleep(1)
            clear()
            return
        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                        Pilihan Tidak Valid                          |")
            print("|         -----------------------------------------------------       |")
            print("|                       Silahkan Pilih Kembali                        |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan enter untuk melanjutkan....")
            clear()
            menu_admin(id_admin)
    except:
        clear()
        print("|         -----------------------------------------------------        |")
        print("|                       TERJADI KESALAHAN INPUTAN                      |")
        print("|         -----------------------------------------------------        |")
        print("|                         Silahkan Coba Kembali                        |")
        print("|         -----------------------------------------------------        |")
        input("Tekan enter untuk melanjutkan....")
        clear()
        menu_admin(id_admin)


def menu_user(id_user):
    try:
        print('''
==================================================
‖                    MENU USER                   ‖
==================================================''')
        print("| 1. Baca Ekosistem Darat                        |")
        print("| 2. Baca Spesies Hewan                          |")
        print("| 3. Baca Spesies Tumbuhan                       |")
        print("| 4. Membuat Laporan                             |")
        print("| 5. Kembali ke Menu Awal                        |")
        print("==================================================")

        choice = input("Pilih menu: ")

        if choice == "1":
            clear()
            darat = EkosistemDarat()
            darat.read_by_user(id_user)
        elif choice == "2":
            clear()
            hewan = spesies_hewan()
            hewan.read_by_user(id_user)
        elif choice == "3":
            clear()
            tumbuhan = spesies_tumbuhan()
            tumbuhan.read_by_user(id_user)
        elif choice == "4":
            clear()
            lapor = laporan()
            lapor.create(id_user)
        elif choice == "5":
            input("Keluar dari menu user....")
            clear()
            return

        else:
            clear()
            print("|         -----------------------------------------------------       |")
            print("|                        Pilihan Tidak Valid                          |")
            print("|         -----------------------------------------------------       |")
            print("|                       Silahkan Pilih Kembali                        |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan enter untuk melanjutkan....")
            clear()
            menu_user(id_user)
    except:
        print("|         -----------------------------------------------------        |")
        print("|                       TERJADI KESALAHAN INPUTAN                      |")
        print("|         -----------------------------------------------------        |")
        print("|                          Silahkan Coba Kembali                       |")
        print("|         -----------------------------------------------------        |")
        input("Tekan enter untuk melanjutkan....")
        clear()
        menu_user(id_user)





#--------------Autorisasi---------------#
def login_admin():
    print('''
==================================================
‖                   LOGIN ADMIN                  ‖
==================================================\n''')
    try:
        nama_admin = input("Masukkan nama admin: ")
        password = pwinput.pwinput(prompt="Masukkan password: ")

        connection = conn()
        if connection:
            cursor = connection.cursor()
            query = "SELECT * FROM admin WHERE nama_admin = %s AND password = %s"
            cursor.execute(query, (nama_admin, password))
            admin = cursor.fetchone()

            if admin:
                clear()
                print("\t\t\t Login Berhasil.....")
                time.sleep(1)
                clear()
                id_admin = admin[0]
                menu_admin(id_admin)
            else:
                clear()
                print("|         -----------------------------------------------------        |")
                print("|                      Nama Admin atau Password Salah                  |")
                print("|         -----------------------------------------------------        |")
                input("\nTekan enter untuk melanjutkan....")
                clear()
            
            cursor.close()
            connection.close()
    except:
        clear()
        print("|         -----------------------------------------------------        |")
        print("|                       TERJADI KESALAHAN INPUTAN                      |")
        print("|         -----------------------------------------------------        |")
        print("|                          Silahkan Coba Kembali                       |")
        print("|         -----------------------------------------------------        |")
        input("Tekan enter untuk melanjutkan....")
        clear()



def login_user():
    print('''
==================================================
‖                   LOGIN USER                   ‖
==================================================\n''')
    try:
        nama_user = input("Masukkan nama user: ")
        password = pwinput.pwinput(prompt="Masukkan password: ")

        connection_db = conn()
        if connection_db:
            cursor = connection_db.cursor()
            query = "SELECT * FROM user WHERE nama_user = %s AND password = %s"
            cursor.execute(query, (nama_user, password))
            user = cursor.fetchone()

            if user:
                clear()
                print("\t\t\t Login Berhasil.....")
                time.sleep(1)
                clear()
                id_user = user[0]  
                menu_user(id_user)
            else:
                clear()
                print("|         -----------------------------------------------------        |")
                print("|               Pengguna Tidak Ditemukan Atau Password Salah           |")
                print("|         -----------------------------------------------------        |")
                input("\nTekan enter untuk melanjutkan....")
                clear()
            
            cursor.close()
            connection_db.close()
    except:
        clear()
        print("|         -----------------------------------------------------        |")
        print("|                       TERJADI KESALAHAN INPUTAN                      |")
        print("|         -----------------------------------------------------        |")
        print("|                          Silahkan Coba Kembali                       |")
        print("|         -----------------------------------------------------        |")
        input("Tekan enter untuk melanjutkan....")
        clear()



def create_user_account():
    print('''
==================================================
‖                 BUAT AKUN USER                 ‖
==================================================\n''')
    nama_user = input("Masukkan nama user: ")
    password = input("Masukkan password 10 angka/huruf: ")
    no_telpon = input("Masukkan nomor telepon 12 angka: ")

    try:
        connection = conn()  
        if connection:
            cursor = connection.cursor()


            user_query_check = "SELECT * FROM user WHERE nama_user = %s OR no_telpon = %s"
            cursor.execute(user_query_check, (nama_user, no_telpon))
            existing_users = cursor.fetchall()

            if existing_users:
                print("|         -----------------------------------------------------        |")
                print("|                        PEMBUATAN AKUN DIBATALKAN                     |")
                print("|         -----------------------------------------------------        |")
                print("|              Nama User atau Nomor Telpon Sudah Digunakan             |")
                print("|         -----------------------------------------------------        |")
                input("\nTekan enter untuk melanjutkan....")
                return

            query_insert = "INSERT INTO user (nama_user, password, no_telpon) VALUES (%s, %s, %s)"
            cursor.execute(query_insert, (nama_user, password, no_telpon))
            connection.commit()
            clear()
            print("|         -----------------------------------------------------        |")
            print("|                          AKUN BERHASIL DIBUAT                        |")
            print("|         -----------------------------------------------------        |")
            input("\nTekan enter untuk melanjutkan....")
            clear()

            cursor.close()
            connection.close()
    except:
        clear()
        print("|         -----------------------------------------------------        |")
        print("|                       TERJADI KESALAHAN INPUTAN                      |")
        print("|         -----------------------------------------------------        |")
        print("|                          Silahkan Coba Kembali                       |")
        print("|         -----------------------------------------------------        |")
        input("Tekan enter untuk melanjutkan....")
        clear()


def main():
    while True:
        clear()
        print('''
==================================================
‖                    MENU LOGIN                  ‖
==================================================''')
        print("| 1. Login user                                  |")
        print("| 2. Login admin                                 |")
        print("| 3. Buat Akun                                   |")
        print("| 0. Keluar                                      |")
        print("==================================================")
        try:
            choice = input("Pilih menu: ")

            if choice == "1":
                clear()
                login_user()
            elif choice == "2":
                clear()
                login_admin()
            elif choice == "3":
                clear()
                create_user_account()
            elif choice == "0":
                clear()
                print("✦======================================================================✦")
                print("|                        PROGRAM TELAH SELESAI                         |")
                print("✦======================================================================✦")
                print("|           TERIMAKASIH TELAH MENGGUNAKAN PROGRAM SEDERHANA            |")
                print("|                      YANG DISUSUN OLEH KELOMPOK 5                    |")
                print("|                         SISTEM INFORMASI A'23                        |")
                print("|                                  |||                                 |")
                print("|                         UNIVERSITAS MULAWARMAN                       |")
                print("✦======================================================================✦")
                input("")
                clear()
                break
            else:
                clear()
                print("|         -----------------------------------------------------        |")
                print("|                          PILIHAN TIDAK VALID                         |")
                print("|         -----------------------------------------------------        |")
                print("|                         Silahkan Pilih Kembali                       |")
                print("|         -----------------------------------------------------        |")
                input("Tekan enter untuk melanjutkan....")
        except:
            clear()
            print("|         -----------------------------------------------------        |")
            print("|                       TERJADI KESALAHAN INPUTAN                      |")
            print("|         -----------------------------------------------------        |")
            print("|                          Silahkan Coba Kembali                       |")
            print("|         -----------------------------------------------------        |")
            input("Tekan enter untuk melanjutkan....")
            clear()




if __name__ == "__main__":
    main()