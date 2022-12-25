import QtQuick 6.0
import QtQuick.Controls	6.0
import QtQuick.Controls.Material 6.0

ApplicationWindow {
    visible: true

    width: 600
    height: 400
    maximumHeight: 400
    maximumWidth: 600
    minimumHeight: 400
    minimumWidth: 600

    title: "Pass Gen"
    id: window

    Material.theme: Material.Dark
    
    Rectangle {
        id: main

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        anchors.topMargin: 0

        color: "#303030"

        TextField {
            id: password

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom

            anchors.rightMargin: 10
            anchors.leftMargin: 10
            anchors.bottomMargin: 335
            anchors.topMargin: 20

            readOnly: true
            placeholderText: "Generated Password"
            font.family: "Courier New"
            font.pixelSize: 30

            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
            focus: true
            baselineOffset: 0
            bottomPadding: 0
            topPadding: 0
        }

        Label {
            id: pass_lenght

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: password.bottom
            anchors.bottom: parent.bottom

            anchors.rightMargin: 349
            anchors.leftMargin: 8
            anchors.bottomMargin: 280
            anchors.topMargin: 24

            text: "Password Lenght:"
            font.family: "Courier New"
            font.pixelSize: 25
        }

        TextField {
            id: password_lenght

            anchors.left: pass_lenght.right
            anchors.right: parent.right
            anchors.top: password.bottom
            anchors.bottom: parent.bottom

            anchors.rightMargin: 200
            anchors.bottomMargin: 272
            anchors.topMargin: 24

            placeholderText: "10 to 32"
            validator: IntValidator {bottom: 10; top: 32}
            font.family: "Courier New"
            font.pixelSize: 25

            horizontalAlignment: Text.AlignLeft
            verticalAlignment: Text.AlignVCenter
            anchors.leftMargin: 10
            bottomPadding: 10
            topPadding: 0
        }

        CheckBox {
            id: locase
            text: qsTr("Lower Case Characters")

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: pass_lenght.bottom
            anchors.bottom: parent.bottom

            font.pointSize: 15
            font.family: "Courier New"

            anchors.rightMargin: 290
            anchors.leftMargin: 10
            anchors.bottomMargin: 225
            anchors.topMargin: 17
        }

        CheckBox {
            id: upcase
            text: qsTr("Upper Case Characters")

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: locase.bottom
            anchors.bottom: parent.bottom

            font.pointSize: 15
            font.family: "Courier New"

            anchors.rightMargin: 290
            anchors.leftMargin: 10
            anchors.bottomMargin: 165
            anchors.topMargin: 20
        }

        CheckBox {
            id: symbol
            text: qsTr("Symbol Characters")

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: upcase.bottom
            anchors.bottom: parent.bottom

            font.family: "Courier New"
            font.pointSize: 15

            anchors.rightMargin: 290
            anchors.leftMargin: 10
            anchors.bottomMargin: 101
            anchors.topMargin: 20
        }

        Button {
            id: button
            text: qsTr("Generate Password")

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom

            font.pointSize: 20
            font.family: "Courier New"

            anchors.bottomMargin: 20
            anchors.topMargin: 325
            anchors.rightMargin: 150
            anchors.leftMargin: 150

            onClicked: {
                var len = parseInt(password_lenght.text)
                var lo = locase.checked
                var up = upcase.checked
                var sym = symbol.checked

                password.text = backend.generate_password(len, lo, up, sym)
            }
        }
    }
}
