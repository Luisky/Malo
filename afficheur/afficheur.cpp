#include "afficheur.h"
#include "ui_afficheur.h"

Afficheur::Afficheur(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Afficheur)
{
    ui->setupUi(this);

    socket.connectToHost("192.168.15.10",502);
    qDebug("Afficheur connecté");

    socket.waitForConnected(3000);
    if(socket.state() != QAbstractSocket::ConnectedState){

        ui->label_3->setText("<font color='red'>Afficheur non connecté</font>");
        socket.close();
        exit(1);
    }

    else ui->label_3->setText("<font color= 'green'>Afficheur connecté</font>");

    connect(ui->pushButton, SIGNAL(clicked(bool)),SLOT(text()));
   // connect(ui->pushButton_2, SIGNAL(clicked(bool)),SLOT(supprimer));

}

void Afficheur::envoieTrame(QString message){

    int lmax=100;
    int i=13;
    if(message.length()>lmax){
        qDebug("Message de 100 caractères maximum");
        exit(1);
    }
    int lt=message.length()+13; //longueur du message + longueur de la trame

    _trameDemande = new unsigned char [lt];
    _trameReponse = new unsigned char [lt];

    //En tête
    _trameDemande[0]=0; //Transaction identifier
    _trameDemande[1]=0;
    _trameDemande[2]=0; //Protocol
    _trameDemande[3]=0;
    _trameDemande[4]=0;
    _trameDemande[5]=message.length()+7;
    _trameDemande[6]=1;

    //Data
    _trameDemande[7]=16;
    _trameDemande[8]=0;
    _trameDemande[9]=1;
    _trameDemande[10]=0;
    _trameDemande[11]=message.length()/2;
    _trameDemande[12]=message.length();

    for(i=13;i<14+message.length();i++){

    _trameDemande[i]=message.toStdString() [i-13]; //Conversion QString en tableau de char
    }

    for(i=0;i<lt;i++){

        socket.write((char*)_trameDemande,lt);
        socket.flush();
    }

    socket.read((char*)_trameReponse, 12);

}

void Afficheur::text(){

    QString msg="";
    int lg, dif;

    QString Ligne1=ui->lineEdit->text();

    lg=Ligne1.length();
    dif=(int) ((20-lg));
    for(int i=0;i<dif;i++){

        msg+=" ";
    }
    msg+=Ligne1;
    for(int i=dif+lg;i<20;i++){
        msg+=" ";
    }
    QString LigneTotale=msg;
    envoieTrame(LigneTotale);
}

Afficheur::~Afficheur()
{
    socket.close();
    delete ui;
    qDebug("Close");
}
