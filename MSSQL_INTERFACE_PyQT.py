from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QTableView,QApplication
import sys
server_name = "localhost"
db_name = "DERECHOS"



def conn():
    connString = ('DSN=ORIGIN;Server=LAPTOP-P79DPE8R;Database=DERECHOS;Trusted_Connection=yes;')
    global db
    db= QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(connString)

    if (db.open()):
        print("connected")
        return True
    else:
        print("not connected")
        return False


def displayData(sqlStatement):
    print("processing query...")
    qry = QSqlQuery(db)
    qry.prepare(sqlStatement)
    qry.exec()

    model = QSqlQueryModel()
    model.setQuery(qry)

    view = QTableView()
    view.setModel(model)
    return view

#if __name__ == '__main__':
def showdb():
    app = QApplication(sys.argv)

    if conn():
        SQL_STATEMENT='SELECT * FROM DERECHOS.dbo.Generador'
        dataView = displayData(SQL_STATEMENT)
        dataView.show()

    app.exit()
    sys.exit(app.exec_())