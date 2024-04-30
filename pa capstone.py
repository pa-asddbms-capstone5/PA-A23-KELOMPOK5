import pwinput
import os
from prettytable import prettytable
import mysql.connector
import random
import time

#--------Common---------#
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def conn():
    try:
        connection = mysql.connector.connect(
            host="103.54.170.117",
            user="paasd", 
            password="Paasd1234!",
            database="paasd"
        )
        return connection
    except mysql.connector.Error as err:
        input("Error:", err)

def err_conn(err):
    print("Error:", err)
    print("|         -----------------------------------------------------       |")
    print("|                      Pembuatan Akun User Gagal                      |")
    print("|         -----------------------------------------------------       |")
    input("\nTekan Enter untuk melanjutkan...")
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

    def _get_middle(self, head):
        if head is None:
            return None
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    # Definisikan metode merge_sort_id_ekosistem di sini
    def merge_sort_id_ekosistem(self, head, order='asc'):
        if head is None or head.next is None:
            return head
        
        middle = self._get_middle(head)
        next_to_middle = middle.next
        
        middle.next = None
        
        left = self.merge_sort_id_ekosistem(head, order)
        right = self.merge_sort_id_ekosistem(next_to_middle, order)
        
        sorted_list = self._merge(left, right, order)
        return sorted_list

    def _merge(self, left, right, order='asc'):
        result = None
        
        if left is None:
            return right
        if right is None:
            return left
        
        if order == 'asc':
            if left.data[0] <= right.data[0]:
                result = left
                result.next = self._merge(left.next, right, order)
            else:
                result = right
                result.next = self._merge(left, right.next, order)
        elif order == 'desc':
            if left.data[0] >= right.data[0]:
                result = left
                result.next = self._merge(left.next, right, order)
            else:
                result = right
                result.next = self._merge(left, right.next, order)
        
        return result
    # Fungsi untuk melakukan jump search berdasarkan nama_ekosistem
    def jump_search_nama_ekosistem(self, target):
        if self.ekosistem_list.head is None:
            print("Linked list kosong.")
            return -1
        
        n = self.ekosistem_list.size()
        step = int(n ** 0.5)
        prev = None
        current = self.ekosistem_list.head
        
        while current and current.data[1] < target:
            prev = current
            for _ in range(step):
                if current.next:
                    current = current.next
                else:
                    break
        
        while current and current.data[1] >= target:
            if current.data[1] == target:
                return current.data
            current = current.prev
        
        return -1

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
                print("\nData berhasil dimasukkan ke database ekosistem darat.")
                # Menambah data ke dalam linked list
                self.ekosistem_list.append((cursor.lastrowid, nama_ekosistem, id_admin, lokasi_geografis, status_ekosistem))
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|            Gagal Memasukan Data ke Database Ekosistem Darat         |")
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
                    print("Tidak ada data ekosistem_darat yang tersedia.")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                cursor.close()
            except mysql.connector.Error as err:
                print("Error:", err)
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
            except mysql.connector.Error as err:
                print("Error:", err)
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
            except mysql.connector.Error as err:
                print("Error:", err)
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
            except mysql.connector.Error as err:
                print("Error:", err)
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
‖             MENU EKOSISTEM DARAT               ‖
==================================================''')
        print("| 1. Create                                      |")
        print("| 2. Read                                        |")
        print("| 3. Update                                      |")
        print("| 4. Delete                                      |")
        print("| 5. Sort                                        |")
        print("| 6. Search                                      |")
        print("| 7. Kembali ke Menu Sebelumnya                  |")
        print("==================================================")

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
            sorted_list_head = self.merge_sort_id_ekosistem(self.ekosistem_list.head, order)
            if sorted_list_head:
                current = sorted_list_head
                table = prettytable.PrettyTable(["id_ekosistem", "nama_ekosistem", "id_admin", "lokasi_geografis", "status_ekosistem"])
            while current:
                table.add_row(current.data)
                current = current.next
            print("Data yang sudah diurutkan:")
            print(table)
        
        elif choice == "6":
            target = input("Masukkan nama ekosistem yang ingin dicari: ")
            result = self.jump_search_nama_ekosistem(target)
            if result != -1:
                print("Data ditemukan:")
                print(result)
            else:
                print("|         -----------------------------------------------------       |")
                print("|                 Tidak Ditemukan Data Ekosistem Darat                |")
                print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        elif choice == "7":
            clear()
            menu_admin(id_admin)


class spesies_hewan:
    def __init__(self):
        self.connection = conn()
        self.hewan_list = DoubleLinkedList()
    
    def search_hewan(self, target):
        if self.hewan_list.head is None:
            print("Linked list spesies hewan kosong.")
            return -1
        
        current = self.hewan_list.head

        while current is not None:
            if current.data[1] == target:
                return current.data
            current = current.next
        
        print(f"Data spesies hewan dengan nama '{target}' tidak ditemukan.")
        return -1

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
                print("\nData berhasil dimasukkan ke database spesies hewan.")
                # Menambah data ke dalam linked list
                self.hewan_list.append((cursor.lastrowid, nama_hewan, id_ekosistem, status_populasi, status_perlindungan))
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            except mysql.connector.Error as err:
                print("Error:", err)
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
            except mysql.connector.Error as err:
                print("Error:", err)
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
            except mysql.connector.Error as err:
                print("Error:", err)
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
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|                Gagal Memperbarui Data Spesies Hewan                 |")
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
            except mysql.connector.Error as err:
                print("Error:", err)
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
‖                MENU SPESIES HEWAN              ‖
==================================================''')
        print("| 1. Create                                      |")
        print("| 2. Read                                        |")
        print("| 3. Update                                      |")
        print("| 4. Delete                                      |")
        print("| 5. Sort                                        |")
        print("| 6. Search                                      |")
        print("| 7. Kembali ke Menu Sebelumnya                  |")
        print("==================================================")

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
            sorted_list_head = self.search_hewan()
            current = sorted_list_head
            while current:
                print(current.data)
                current = current.next
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        elif choice == "6":
            target = input("Masukkan nama Hewan yang ingin dicari: ")
            result = self.search_hewan(target)
            if result != -1:
                print("Data ditemukan:")
                print(result)
            else:
                print("|         -----------------------------------------------------       |")
                print("|                         Data Tidak Ditemukan                        |")
                print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        elif choice == "7":
            clear()
            menu_admin(id_admin)


class spesies_tumbuhan:
    def __init__(self):
        self.connection = conn()
        self.tumbuhan_list = DoubleLinkedList()
        
        
    def search_tumbuhan(self, target):
        if self.tumbuhan_list.head is None:
            print("Linked list spesies tumbuhan kosong.")
            return -1
        
        current = self.tumbuhan_list.head

        while current is not None:
            if current.data[1] == target:
                return current.data
            current = current.next
        
        print(f"Data spesies tumbuhan dengan nama '{target}' tidak ditemukan.")
        return -1

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
                print("\nData berhasil dimasukkan ke database spesies tumbuhan.")
                # Menambah data ke dalam linked list
                self.tumbuhan_list.append((cursor.lastrowid, nama_tumbuhan, id_ekosistem, status_populasi, status_perlindungan))
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            except mysql.connector.Error as err:
                print("Error:", err)
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
            except mysql.connector.Error as err:
                print("Error:", err)
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
            except mysql.connector.Error as err:
                print("Error:", err)
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
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|                 Gagal Memperbarui Data Spesies Tumbuhan             |")
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
            except mysql.connector.Error as err:
                print("Error:", err)
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
        print("| 7. Kembali ke Menu Sebelumnya                                      |")
        print("==================================================")
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
            sorted_list_head = self.merge_sort_id_ekosistem()
            current = sorted_list_head
            while current:
                print(current.data)
                current = current.next
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        elif choice == "6":
            target = input("Masukkan nama Tumbuhan yang ingin dicari: ")
            result = self.search_tumbuhan(target)
            if result != -1:
                print("Data ditemukan:")
                print(result)
            else:
                print("|         -----------------------------------------------------       |")
                print("|                           Data Tidak Ditemukan                      |")
                print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)
        elif choice == "7":
            clear()
            menu_admin(id_admin)


class laporan:
    def __init__(self):
        self.connection = conn()
        self.laporan_list = DoubleLinkedList()

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
                        print("\nIsi laporan:", isi_laporan)
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
                        print("|         -----------------------------------------------------       |")
                        print("|          Tidak Ada Admin Yang Tersedia Untuk Membuat Laporan        |")
                        print("|         -----------------------------------------------------       |")
                        input("Tekan Enter untuk melanjutkan...")
                        clear()
                        menu_user(id_user)
                except mysql.connector.Error as err:
                    print("Error:", err)
                    print("|         -----------------------------------------------------       |")
                    print("|                           Gagal Membuat Laporan                     |")
                    print("|         -----------------------------------------------------       |")
                    input("Tekan Enter untuk melanjutkan...")
                    clear()
                    menu_user(id_user)
                finally:
                    cursor.close()
                    self.connection.close()
            else:
                print("|         -----------------------------------------------------       |")
                print("|                   Tidak Dapat Terhubung Ke Database                 |")
                print("|         -----------------------------------------------------       |")
                input("Tekan enter untuk melanjutkan...")
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
                        for data in laporan:  
                            table.add_row(data)
                        print(table)
                        input("Tekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                    else:
                        print("|         -----------------------------------------------------       |")
                        print("|                     Data Laporan Tidak Tersedia                     |")
                        print("|         -----------------------------------------------------       |")
                        clear()
                        self.menu(id_admin)
                except mysql.connector.Error as err:
                    print("Error:", err)
                    print("|         -----------------------------------------------------       |")
                    print("|                       Data Laporan Gagal Dibaca                     |")
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
                        print("|         -----------------------------------------------------       |")
                        print("|               Laporan Dengan ID Tersebut Tidak Ditemukan              |")
                        print("|         -----------------------------------------------------       |")
                        input("Tekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)

                except mysql.connector.Error as err:
                    print("Error:", err)
                    print("|         -----------------------------------------------------       |")
                    print("|                    Gagal Memperbarui Data Laporan                   |")
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
                        self.menu(id_admin)
                        clear()
                    else:
                        print("|         -----------------------------------------------------       |")
                        print("|                             Data Gagal Di Hapus                     |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan enter untuk melanjutkan....")
                        clear()
                        self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|             Data Laporan Dengan ID Tersebut Tidak Ditemukan         |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan enter untuk melanjutkan....")
                    self.menu(id_admin)

            except mysql.connector.Error as err:
                print("Error:", err)
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
            print("| 1. Baca Laporan                                |")
            print("| 2. Update Laporan                              |")
            print("| 3. Hapus Laporan                               |")
            print("| 4. Kembali ke Menu Sebelumnya                  |")
            print("==================================================")

            user_choice = input("Pilih menu: ")

            if user_choice == "1":
                self.read(id_admin)
            elif user_choice == "2":
                self.update(id_admin)
            elif user_choice == "3":
                self.delete(id_admin)
            elif user_choice == "4":
                clear()
                menu_admin(id_admin)
            else:
                print("|         -----------------------------------------------------       |")
                print("|                        Pilihan Tidak Valid                          |")
                print("|         -----------------------------------------------------       |")
                print("|                       Silahkan Pilih Kembali                        |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan enter untuk melanjutkan....")


class user:
    def __init__(self):
        self.connection = conn()
        self.user_list = DoubleLinkedList()

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
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|                        Gagal Menemukan Data User                    |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
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
                user_data = cursor.fetchall()
                if user_data:
                    table = prettytable.PrettyTable(["id_user", "nama_user", "password", "no_telpon"])
                    for user_row in user_data:
                        table.add_row(user_row)
                    print(table)
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|                      Data User Tidak Tersedia                       |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    self.menu(id_admin)
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|                        Data User Gagal Dibaca                      |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu user...")
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
                    print("|         -----------------------------------------------------       |")
                    print("|               User Dengan ID Tersebut Tidak Ditemukan               |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu user...")
                    clear()
                    self.menu(id_admin)
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|                       Data User Gagal Diperbarui                    |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
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
                        print("|         -----------------------------------------------------       |")
                        print("|                   Penghapusan Data User Dibatalkan                  |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu user...")
                        clear()
                        self.menu(id_admin)
                else:
                    print("Tidak ditemukan data user dengan ID tersebut.")
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|                         Data User Gagal Dihapus                     |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu user...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung Ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu user...")
            clear()
            self.menu(id_admin)

    def menu(self, id_admin):
        print('''
=====================================================
‖                 MENU ADMINISTRASI USER            ‖
=====================================================''')
        print("| 1. Create User                                    |")
        print("| 2. Read User                                      |")
        print("| 3. Update User                                    |")
        print("| 4. Delete User                                    |")
        print("| 5. Kembali ke Menu Sebelumnya                     |")
        print("=====================================================")

        user_choice = input("Pilih menu: ")

        if user_choice == "1":
            clear()
            self.create_by_admin(id_admin)
        elif user_choice == "2":
            clear()
            self.read(id_admin)
        elif user_choice == "3":
            clear()
            self.update(id_admin)
        elif user_choice == "4":
            clear()
            self.delete(id_admin)
        elif user_choice == "5":
            clear()
            menu_admin(id_admin)
        else:
            print("|         -----------------------------------------------------       |")
            print("|                        Pilihan Tidak Valid                          |")
            print("|         -----------------------------------------------------       |")
            print("|                       Silahkan Pilih Kembali                        |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan enter untuk melanjutkan....")



class admin:
    def __init__(self):
        self.connection = conn()
        self.admin_list = DoubleLinkedList()

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
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|                      Data Admin Gagal Dimasukkan                    |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
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
                query = "SELECT * FROM admin"
                cursor.execute(query)
                admin_data = cursor.fetchall()
                if admin_data:
                    table = prettytable.PrettyTable(["id_admin", "nama_admin", "password", "no_telpon"])
                    for admin_row in admin_data:
                        table.add_row(admin_row)
                    print(table)
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|                       Data Admin Tidak Tersedia                     |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|                        Data Admin Gagal Dibaca                      |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
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
                    print("|         -----------------------------------------------------       |")
                    print("|               Admin Dengan ID Tersebut Tidak Ditemukan              |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
                    clear()
                    self.menu(id_admin)
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|                     Gagal Memperbarui Data Admin                    |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
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
                        print("|         -----------------------------------------------------       |")
                        print("|                   Penghapusan Data Admin Dibatalkan                 |")
                        print("|         -----------------------------------------------------       |")
                        input("\nTekan Enter untuk kembali ke menu admin...")
                        clear()
                        self.menu(id_admin)
                else:
                    print("|         -----------------------------------------------------       |")
                    print("|            Data Admin Dengan ID Tersebut Tidak Ditemukan            |")
                    print("|         -----------------------------------------------------       |")
                    input("\nTekan Enter untuk kembali ke menu admin...")
            except mysql.connector.Error as err:
                print("Error:", err)
                print("|         -----------------------------------------------------       |")
                print("|                       Gagal Menghapus Data Admin                    |")
                print("|         -----------------------------------------------------       |")
                input("\nTekan Enter untuk kembali ke menu admin...")
                clear()
                self.menu(id_admin)
            finally:
                cursor.close()
        else:
            print("|         -----------------------------------------------------       |")
            print("|                   Tidak Dapat Terhubung ke Database                 |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan Enter untuk kembali ke menu admin...")
            clear()
            self.menu(id_admin)

    def menu(self, id_admin):
        print('''
=====================================================
‖               MENU ADMINISTRASI ADMIN             ‖
=====================================================''')
        print("| 1. Create Admin                                   |")
        print("| 2. Read Admin                                     |")
        print("| 3. Update Admin                                   |")
        print("| 4. Delete Admin                                   |")
        print("| 5. Kembali ke Menu Sebelumnya                     |")
        print("=====================================================")

        user_choice = input("Pilih menu: ")

        if user_choice == "1":
            clear()
            self.create(id_admin)
        elif user_choice == "2":
            clear()
            self.read(id_admin)
        elif user_choice == "3":
            clear()
            self.update(id_admin)
        elif user_choice == "4":
            clear()
            self.delete(id_admin)
        elif user_choice == "5":
            clear()
            menu_admin(id_admin)
        else:
            print("|         -----------------------------------------------------       |")
            print("|                        Pilihan Tidak Valid                          |")
            print("|         -----------------------------------------------------       |")
            input("\nTekan enter untuk melanjutkan....")



#------------Admin------------#
def menu_admin(id_admin):
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

    user_choice = input("Pilih menu: ")

    if user_choice == "1":
        clear()
        darat = EkosistemDarat()
        darat.menu(id_admin)
    elif user_choice == "2":
        clear()
        hewan = spesies_hewan()
        hewan.menu(id_admin)  # Pastikan objek hewan dibuat sebelum pemanggilan metode menu
    elif user_choice == "3":
        clear()
        tumbuhan = spesies_tumbuhan()
        tumbuhan.menu(id_admin)
    elif user_choice == "4":
        clear()
        lapor = laporan()
        lapor.menu(id_admin)
    elif user_choice == "5":
        clear()
        userr = user()
        userr.menu(id_admin)
    elif user_choice == "6":
        clear()
        adminn = admin()
        adminn.menu(id_admin)
    elif user_choice == "7":
        clear()
        print("\t\t\t Keluar dari Menu Admin.....")
        time.sleep(1)
        clear()
        return

    else:
        print("|         -----------------------------------------------------       |")
        print("|                        Pilihan Tidak Valid                          |")
        print("|         -----------------------------------------------------       |")
        print("|                       Silahkan Pilih Kembali                        |")
        print("|         -----------------------------------------------------       |")
        input("\nTekan enter untuk melanjutkan....")
        clear()
        menu_admin(id_admin)

def menu_user(id_user):
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

    user_choice = input("Pilih menu: ")

    if user_choice == "1":
        clear()
        darat = EkosistemDarat()
        darat.read_by_user(id_user)
    elif user_choice == "2":
        clear()
        hewan = spesies_hewan()
        hewan.read_by_user(id_user)
    elif user_choice == "3":
        clear()
        tumbuhan = spesies_tumbuhan()
        tumbuhan.read_by_user(id_user)
    elif user_choice == "4":
        clear()
        lapor = laporan()
        lapor.create(id_user)
    elif user_choice == "5":
        clear()
        print("\t\t\t Keluar dari Menu User.....")
        time.sleep(1)
        clear()
        return

    else:
        print("|         -----------------------------------------------------       |")
        print("|                        Pilihan Tidak Valid                          |")
        print("|         -----------------------------------------------------       |")
        print("|                       Silahkan Pilih Kembali                        |")
        print("|         -----------------------------------------------------       |")
        input("\nTekan enter untuk melanjutkan....")
        clear()
        menu_user(id_user)




#--------------Autorisasi---------------#
def login_admin():
    print('''
==================================================
‖                   LOGIN ADMIN                  ‖
==================================================\n''')
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
            id_admin = admin[0]  # Ambil ID user dari hasil query
            menu_admin(id_admin)  # Teruskan ID user ke fungsi menu_user()
        else:
            print("|         -----------------------------------------------------        |")
            print("|                      Nama Admin atau Password Salah                  |")
            print("|         -----------------------------------------------------        |")
            input("\nTekan enter untuk melanjutkan....")
            clear()
        
        cursor.close()
        connection.close()


def login_user():
    print('''
==================================================
‖                   LOGIN USER                   ‖
==================================================\n''')
    nama_user = input("Masukkan nama user: ")
    password = pwinput.pwinput(prompt="Masukkan password: ")

    connection_db = conn()  # Menggunakan nama yang berbeda untuk fungsi dan variabel
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
            id_user = user[0]  # Ambil ID user dari hasil query
            menu_user(id_user)
        else:
            print("|         -----------------------------------------------------        |")
            print("|              Nama User atau Nomor Telpon Sudah Digunakan             |")
            print("|         -----------------------------------------------------        |")
            input("\nTekan enter untuk melanjutkan....")
            clear()
        
        cursor.close()
        connection_db.close()  # Tutup koneksi setelah digunakan


def create_user_account():
    print('''
==================================================
‖                 BUAT AKUN USER                 ‖
==================================================\n''')
    nama_user = input("Masukkan nama user: ")
    password = input("Masukkan password 10 angka/huruf: ")
    no_telpon = input("Masukkan nomor telepon 12 angka: ")

    connection = connection()
    if connection:
        cursor = connection.cursor()

        # Periksa apakah nama user atau nomor telepon sudah ada di database
        user_query_check = "SELECT * FROM user WHERE nama_user = %s OR no_telpon = %s"
        cursor.execute(user_query_check, (nama_user, no_telpon))
        existing_users = cursor.fetchall()

        if existing_users:
            print("\n|         -----------------------------------------------------        |")
            print("|                        PEMBUATAN AKUN DIBATALKAN                     |")
            print("|         -----------------------------------------------------        |")
            print("|              Nama User atau Nomor Telpon Sudah Digunakan             |")
            print("|         -----------------------------------------------------        |")
            input("\nTekan enter untuk melanjutkan....")
            return

        # Jika nama user dan nomor telepon unik, masukkan ke database
        query_insert = "INSERT INTO user (nama_user, password, no_telpon) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query_insert, (nama_user, password, no_telpon))
            connection.commit()
            print("\n|         -----------------------------------------------------        |")
            print("|                          AKUN BERHASIL DIBUAT                        |")
            print("|         -----------------------------------------------------        |")
            input("\nTekan enter untuk melanjutkan....")
            clear()
        except mysql.connector.Error as err:
            err_conn(err)
        
        cursor.close()
        connection.close()

def create_admin_account():
    print('''
==================================================
‖                 BUAT AKUN ADMIN                ‖
==================================================\n''')
    nama_admin = input("Masukkan nama admin: ")
    password = input("Masukkan password 10 angka/huruf: ")
    no_telpon = input("Masukkan nomor telepon 12 angka: ")
    kode_admin = input("Masukkan kode admin: ")

    if kode_admin != "192193":
        print("\n|         -----------------------------------------------------        |")
        print("|                             KODE ADMIN SALAH                         |")
        print("|         -----------------------------------------------------        |")
        print("|                        PEMBUATAN AKUN DIBATALKAN                     |")
        print("|         -----------------------------------------------------        |")
        input("Tekan enter untuk melanjutkan ...")
        return

    connection = connection()
    if connection:
        cursor = connection.cursor()

        # Periksa apakah ada akun admin dengan nama atau nomor telepon yang sama
        query_check = "SELECT * FROM admin WHERE nama_admin = %s OR no_telpon = %s"
        cursor.execute(query_check, (nama_admin, no_telpon))
        existing_admins = cursor.fetchall()

        if existing_admins:
            clear()
            print("\n|         -----------------------------------------------------        |")
            print("|                        PEMBUATAN AKUN DIBATALKAN                     |")
            print("|         -----------------------------------------------------        |")
            print("|             Nama Admin atau Nomor Telpon Sudah Digunakan             |")
            print("|         -----------------------------------------------------        |")
            input("\nTekan enter untuk melanjutkan....")
            return

        # Jika kode admin benar dan nama admin serta nomor telepon belum digunakan, masukkan ke database
        query_insert = "INSERT INTO admin (nama_admin, password, no_telpon) VALUES (%s, %s, %s)"
        try:
            cursor.execute(query_insert, (nama_admin, password, no_telpon))
            connection.commit()
            print("|         -----------------------------------------------------        |")
            print("|                       PEMBUATAN AKUN BERHASIL                        |")
            print("|         -----------------------------------------------------        |")
            input("Tekan enter untuk melanjutkan ...")
            clear()
        except mysql.connector.Error as err:
            clear() #kalau bagian ini ada kehapus berarti tempat clearnya salah
            print("Error:", err)
            print("|         -----------------------------------------------------        |")
            print("|                         PEMBUATAN AKUN GAGAL                         |")
            print("|         -----------------------------------------------------        |")
            return
        
        cursor.close()
        connection.close()


def main():
    while True:
        clear()
        print("+====================================================================+")
        print("|                           SELAMAT DATANG                           |")
        print("|   DI PROGRAM SISTEM INFORMASI EKOSISTEM DARAT DI KALIMANTAN TIMUR  |")
        print("|    OLEH : KELOMPOK 5 - SISTEM INFORMASI - UNIVERSITAS MULAWARMAN   |")
        print("+====================================================================+")
        print("| 1. Login user                                                      |")
        print("| 2. Login admin                                                     |")
        print("| 3. Buat Akun                                                       |")
        print("| 0. Keluar                                                          |")
        print("+====================================================================+")

        choice = input("Pilih menu: ")

        if choice == "1":
            clear()
            login_user()
        elif choice == "2":
            clear()
            login_admin()
        elif choice == "3":
            clear()
            # create_user_account()
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
            quit()
        else:
            clear()
            print("|         -----------------------------------------------------        |")
            print("|                          PILIHAN TIDAK VALID                         |")
            print("|         -----------------------------------------------------        |")
            print("|                         Silahkan Pilih Kembali                       |")
            print("|         -----------------------------------------------------        |")
            input("Tekan enter untuk melanjutkan....")

if __name__ == "__main__":
    main()
