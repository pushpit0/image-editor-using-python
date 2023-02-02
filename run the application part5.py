# initialize the ImageEditorClass and run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = ImageEditorClass()
    myapp.showMaximized()
    sys.exit(app.exec_())
