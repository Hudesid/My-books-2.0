from django.shortcuts import HttpResponse

def main(request):
    show = """
           <h1>Kitoblar ro'yxati</h1>
           <li><a href="book/1">Kichik shahzoda</a>
           <li><a href="book/2">Moby-Dick</a>
           <li><a href="book/3">Oʻtkan kunlar</a>
    """
    return HttpResponse(show)

def first_book(request):
    book_1 = """
            <h1>Kichik shahzoda</h1>
            <h3>Author: Antuan de Sent-Ekzyuperi</h3>
            <h3>Publication date: April 1943 (U.S.: English & French) 1945 (France: French)</h3>
            <h3>Genre: Science fantasy</h3>
            <p>„Kichik shahzoda“ (fransuzcha: Le Petit Prince) – allegorik ertak, Antuan de Sent-Ekzyuperining eng mashhur asari. Asarda Kichkina shahzoda koinotdagi turli sayyoralarga, shu oʻrinda, Yerga tashrif buyurganligi haqida hikoya qilinadi. 
            Kitob yolgʻizlik, doʻstlik, sevgi va yoʻqotish mavzulariga bagʻishlangan. Bolalar kitobining uslubiga qaramay, uning qahramoni hayot va inson tabiati haqida hikoya qiladi.
            Birinchi marta 1943-yil 6-aprelda Nyu-Yorkda nashr etilgan. U butun dunyo boʻylab 140 million nusxadan koʻp sotilgan va eng koʻp xarid qilingan kitoblar roʻyxatidan joy egallagan. Kitobdagi rasmlar muallifning oʻzi tomonidan yaratilgan. 
            Bu tasvirlar asarning asosiy qismidir: ertak qahramonlarining oʻzlari chizmalarga murojaat qiladilar va ular haqida bahslashadilar. „Kichik shahzoda“dagi noyob tasvirlar til to‘siqlarini yo‘q qiladi va hamma tushuna oladigan koʻrinishda boʻladi. 
            Antuan de Sent-Ekzyuperi kitob haqida shunday deydi: „Axir, barcha kattalar dastlab bolalar edi, ulardan faqat bir nechtasi buni eslaydi“.</p>
    <a href ="../">Book to list</a>
    """

    return HttpResponse(book_1)


def second_book(request):
    book_2 = """
            <h1>Moby-Dick</h1>
            <h3>Author: Herman Melville</h3>
            <h3>Publication date: October 18, 1851 (United Kingdom) November 14, 1851 (U.S.)</h3>
            <h3>Genre: Adventure, fiction, epic, sea, story, encyclopedic, novel</h3>
            <p>„Moby-Dick; or, The Whale“ (tarjimasi „Mobi Dik, yoxud (Oq) kit“) – amerikalik yozuvchi Herman Melville yozgan roman. Ilk bor 1851-yil chop etilgan.
            Asar Ishmael nomidan yozilgan boʻlib, unda „Pequod“ kemasi kapitani Ahab kemaning oldingi safarida oyogʻini tishlab, uzib olgan oq kashalot – Moby Dickdan qasos olish uchun chiqqan dengiz safari haqida hikoya qilinadi.
            Amerika adabiy renessansi davrida yozilgan ushbu roman dastlab taqrizchilar tomonidan turlicha kutib olingan, bozori kasod boʻlgan, muallif 1891-yil vafot etgan yilda nashrdan chiqmay qoʻygan boʻlgan.
            XX asrga kelib, xususan, muallif tavalludiga yuz yil toʻlganidan keyin „Moby-Dick“ Buyuk Amerika romani oʻlaroq shuhrat qozongan. Yozuvchi William Faulkner romanni oʻzi yozmaganidan afsusda ekanini izhor qilgan, D. H. Lawrence esa „dunyodagi eng gʻalati va eng ajoyib kitoblardan biri“ deya olqishlagan.
            Romanning ilk jumlasi – „Menga Ishmael (Ismoil) deb murojaat qil“ (inglizcha: Call me Ishmael) jahon adabiyotidagi eng taniqli debochalardan biridir.</p>
            <a href="../">Book to list</a>
    """
    return HttpResponse(book_2)

def third_book(request):
    book_3 = """
    <h>Oʻtkan kunlar</h1>
    <h3>Author: Abdulla Qodiriy</h3>
    <h3>Publication date: 1926-year</h3>
    <h3>Genre: Roman</h3>
    <p>Roman XIX asr voqealarini oʻz ichiga olgan. Murakkab tarixiy hodisalar romanning bosh qahramonlari Otabek va Kumushbibining fojiaviy sevgi qissasi atrofida ifodalangan.
    Voqealar rivoji mahalliy hukmdorlarning hokimiyat uchun qonli kurashlari muhitida kechadi.
    Boshqa yirik epik asarlardagi kabi „Oʻtkan kunlar“da ham hikoyanavislikning koʻp planliligi, ikkilamchi sujetlar mavjudligi, ketma-ket avj oluvchi va fojiali yakun topuvchi voqealar mavjud.

    Ilgʻor fikrlarni olgʻa suruvchi Otabek obrazi romanning gʻoyaviy va kompozitsion markazi hisoblanadi.
    U savdodagi eskirgan iqtisodiy munosabatlarga qarshi chiqib, oila va turmush muammolariga yangi qarashga amal qiladi.
    Adabiyotshunoslar Abdulla Qodiriy oʻz qahramoni nomidan oʻzining shaxsiy oʻy-fikrlarini soʻzlagan, deb bilishadi.</p>
    <a href="../">Book to list</a>
    """
    return HttpResponse(book_3)


