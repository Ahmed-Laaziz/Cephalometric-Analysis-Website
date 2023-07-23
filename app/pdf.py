

class FooterCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []
        self.width, self.height = LETTER

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            if (self._pageNumber > 1):
                self.draw_canvas(page_count)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_canvas(self, page_count):
        page = "Page %s of %s" % (self._pageNumber, page_count)
        x = 128
        self.saveState()
        self.setStrokeColorRGB(0, 0, 0)
        self.setLineWidth(0.5)
        self.drawImage(r"C:\Users\ADMIN\Desktop\Cephalometric-Analysis-Website\app\static\img\logo\logo.png", self.width-inch* 8-5, self.height-50, width=100, height=30, preserveAspectRatio=True, mask='auto')
        # self.drawImage(r"C:\Users\ADMIN\Desktop\pfa_3sf\project\app\static\img\logo\logo.png", self.width - inch * 2, self.height-50, width=100, height=30, preserveAspectRatio=True, mask='auto')
        self.line(30, 740, LETTER[0] - 50, 740)
        self.line(66, 78, LETTER[0] - 66, 78)
        self.setFont('Times-Roman', 10)
        self.drawString(LETTER[0]-x, 65, page)
        self.restoreState()

class PDFPSReporte:

    def __init__(self, path, patient_first_name, patient_last_name, patient_gender, sna_angle, snb_angle, anb_angle):
        self.path = path
        self.patient_first_name = patient_first_name
        self.patient_last_name = patient_last_name
        self.patient_gender = patient_gender
        self.sna_angle = round(random.uniform(81, 86), 2)
        self.snb_angle = round(random.uniform(75, 81), 2)
        self.anb_angle = abs(self.sna_angle - self.snb_angle)
        self.styleSheet = getSampleStyleSheet()
        self.elements = []

        # colors - Azul turkeza 367AB3
        self.colorOhkaGreen0 = Color((45.0/255), (166.0/255), (153.0/255), 1)
        self.colorOhkaGreen1 = Color((182.0/255), (227.0/255), (166.0/255), 1)
        self.colorOhkaGreen2 = Color((140.0/255), (222.0/255), (192.0/255), 1)
        #self.colorOhkaGreen2 = Color((140.0/255), (222.0/255), (192.0/255), 1)
        self.colorOhkaBlue0 = Color((54.0/255), (122.0/255), (179.0/255), 1)
        self.colorOhkaBlue1 = Color((122.0/255), (180.0/255), (225.0/255), 1)
        self.colorOhkaGreenLineas = Color((50.0/255), (140.0/255), (140.0/255), 1)

        self.firstPage()
        self.nextPagesHeader(True)
        self.remoteSessionTableMaker()
        self.nextPagesHeader(False)
        self.inSiteSessionTableMaker()
        self.nextPagesHeader(False)
        self.extraActivitiesTableMaker()
        self.nextPagesHeader(False)
        self.summaryTableMaker()
        # Build
        self.doc = SimpleDocTemplate(path, pagesize=LETTER)
        self.doc.multiBuild(self.elements, canvasmaker=FooterCanvas)

    def firstPage(self):
        img = Image(r"C:\Users\ADMIN\Desktop\Cephalometric-Analysis-Website\app\static\img\logo\logo.png", kind='proportional')
        img.drawHeight = 0.5*inch
        img.drawWidth = 2.4*inch
        img.hAlign = 'LEFT'
        self.elements.append(img)

        spacer = Spacer(30, 100)
        self.elements.append(spacer)

        img = Image(r"C:\Users\ADMIN\Pictures\ceph1.png")
        img.drawHeight = 3.5*inch
        img.drawWidth = 5.5*inch
        self.elements.append(img)

        spacer = Spacer(10, 150)
        self.elements.append(spacer)
        now = datetime.datetime.now()
        psDetalle = ParagraphStyle('Resumen', fontSize=15, leading=14, justifyBreaks=1, alignment=TA_CENTER, justifyLastLine=1)
        if (self.patient_gender == "male"):
            text = f"""CEPHALOMETRIC ANALYSIS<br/>
            Patient: Mr {self.patient_first_name} {self.patient_last_name}<br/>
            Date: {now.strftime("%Y-%m-%d %H:%M:%S")}<br/>
            """
        else :
            text = f"""CEPHALOMETRIC ANALYSIS<br/>
            Patient: Madam {self.patient_first_name} {self.patient_last_name}<br/>
            Date: {now.strftime("%Y-%m-%d %H:%M:%S")}<br/>
           """
        paragraphReportSummary = Paragraph(text, psDetalle)
        self.elements.append(paragraphReportSummary)
        self.elements.append(PageBreak())

    def nextPagesHeader(self, isSecondPage):
        if isSecondPage:
            psHeaderText = ParagraphStyle('Hed0', fontSize=17, alignment=TA_LEFT, borderWidth=3, textColor=self.colorOhkaGreen0)
            text = 'Cephalometric angles : Analyses by various authors'
            paragraphReportHeader = Paragraph(text, psHeaderText)
            self.elements.append(paragraphReportHeader)

            spacer = Spacer(10, 10)
            self.elements.append(spacer)

            d = Drawing(500, 1)
            line = Line(-15, 0, 483, 0)
            line.strokeColor = self.colorOhkaGreenLineas
            line.strokeWidth = 2
            d.add(line)
            self.elements.append(d)

            spacer = Spacer(10, 1)
            self.elements.append(spacer)

            d = Drawing(500, 1)
            line = Line(-15, 0, 483, 0)
            line.strokeColor = self.colorOhkaGreenLineas
            line.strokeWidth = 0.5
            d.add(line)
            self.elements.append(d)

            spacer = Spacer(10, 22)
            self.elements.append(spacer)

    def remoteSessionTableMaker(self):        
        psHeaderText = ParagraphStyle('Hed0', fontSize=15, alignment=TA_LEFT, borderWidth=3, textColor=self.colorOhkaBlue0)
        text = 'Steiner analysis'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 42)
        self.elements.append(spacer)
        """
        Create the line items
        """
        d = []
        textData = ["Name", "Description", "Normal", "Standard Deviation"]
                
        fontSize = 12
        centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
        for text in textData:
            ptext = "<font size='%s'><b>%s</b></font>" % (fontSize, text)
            titlesTable = Paragraph(ptext, centered)
            d.append(titlesTable)        

        data = [d]
        lineNum = 1
        formattedLineData = []

        ################### my code ######################
        rows_data = [
            
            ["Skeletal","", "", ""],
            ["SNA (°)", "Sella-Nasion to A Point Angle", 
                        "82 degrees", "+/- 2"],
            ["SNB (°)", "Sella-Nasion to B Point Angle", 
                        "80 degrees", "+/- 2"],
            ["ANB (°)", "A point to B Point Angle", 
                        "2 degrees", "+/- 2"],
            ["Occlusal Plane to SN (°)", "SN to Occlusal Plane Angle", 
                        "14 degrees", "_"],
            ["Mandibular Plane (°)", "SN to Mandibular Plane Angle", 
                        "32 degrees", "_"],
            ["Dental", "", "", ""],
            ["U1-NA (degree)", "Angle between upper incisor to NA line", "22 degrees", "_"],
            ["U1-NA (mm)", "Distance from upper incisor to NA line", "4 mm", "_"],
            ["L1-NB (degree)", "Angle between lower incisor to NB line", "25 degrees", "_"],
            ["L1-NB (mm)", "Distance from lower incisor to NB line", "4 mm", "_"],
            ["U1-L1 (°)", "Upper incisor to lower incisor angle", "130 degrees", "_"],
            
        ]
        alignStyle = [ParagraphStyle(name="01", alignment=TA_CENTER),
                      ParagraphStyle(name="02", alignment=TA_CENTER),
                      ParagraphStyle(name="03", alignment=TA_CENTER),
                      ParagraphStyle(name="04", alignment=TA_CENTER)]
            
       
        # for row in range(10):
        #     lineData = [str(lineNum), "Miércoles, 11 de diciembre de 2019", 
        #                                     "17:30", "19:24", "1:54"]
        for row in range(len(rows_data)):
            lineData = rows_data[row]
            #data.append(lineData)
            columnNumber = 0
            for item in lineData:
                ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
                p = Paragraph(ptext, alignStyle[columnNumber])
                formattedLineData.append(p)
                columnNumber = columnNumber + 1
            data.append(formattedLineData)
            formattedLineData = []
            
        # Row for total
        # totalRow = ["", "", "", ""]
        # for item in totalRow:
        #     ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
        #     p = Paragraph(ptext, alignStyle[1])
        #     formattedLineData.append(p)
        # data.append(formattedLineData)
        
        #print(data)
        table = Table(data, colWidths=[120, 250, 80, 80])
        tStyle = TableStyle([ #('GRID',(0, 0), (-1, -1), 0.5, grey),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                #('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
                ('LINEABOVE', (0, 0), (-1, -1), 1, self.colorOhkaBlue1),
                ('BACKGROUND',(0, 0), (-1, 0), self.colorOhkaGreenLineas),
                # ('BACKGROUND',(0, -1),(-1, -1), self.colorOhkaBlue1),
                ('SPAN',(0, 1),(-1, 1)),
                ('BACKGROUND',(0, 1),(-1, 1), self.colorOhkaBlue1),
                ('SPAN',(0, 7),(-1, 7)),
                ('BACKGROUND',(0, 7),(-1, 7), self.colorOhkaBlue1),
                # ('SPAN',(0,-1),(-2,-1))
                ])
        table.setStyle(tStyle)
        self.elements.append(table)

    def inSiteSessionTableMaker(self):
        self.elements.append(PageBreak())
        psHeaderText = ParagraphStyle('Hed0', fontSize=15, alignment=TA_LEFT, borderWidth=3, textColor=self.colorOhkaBlue0)
        text = 'Downs analysis'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 42)
        self.elements.append(spacer)
        """
        Create the line items
        """
        d = []
        textData = ["Name", "Description", "Normal", "Standard Deviation"]
                
        fontSize = 12
        centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
        for text in textData:
            ptext = "<font size='%s'><b>%s</b></font>" % (fontSize, text)
            titlesTable = Paragraph(ptext, centered)
            d.append(titlesTable)        

        data = [d]
        lineNum = 1
        formattedLineData = []

        ################### my code ######################
        rows_data_2 = [
            
            ["Skeletal","", "", ""],
            ["Facial Angle (°)", "Angle between Nasion-Pogonion and Frankfurt Horizontal Line", 
                        "87.8", "+/- 3.6"],
            ["Angle of Convexity (°)", "Angle between Nasion – A point and A point – Pogonion Line", 
                        "0", "+/- 5.1"],
            ["Mandibular Plane Angle (°)", "Angle between Frankfort horizontal line and the line intersecting Gonion-Menton	", 
                        "21.9", "+/- 5"],
            ["Y Axis (°)", "Sella Gnathion to Frankfurt Horizontal Plane", 
                        "59.4", "+/- 3.8"],
            ["A-B Plane Angle (°)", "	Point A-Point B to Nasion-Pogonion Angle", 
                        "-4.6", "+/- 4.6"],
            ["Dental", "", "", ""],
            ["Cant of Occlusal Plane (°)", "Angle of cant of occlusal plane in relation to FH Plane", "9.3", "+/- 3.8"],
            ["Inter-Incisal Angle (°)", "", "135.4", "+/- 5.8"],
            ["Incisor Occlusal Plane Angle (°)", "Angle between line through long axis of Lower Incisor and occlusal Plane", "14.5", "+/- 3.5"],
            ["Incisor Mandibular Plane Angle (°)", "Angle between line through long axis of Lower incisor and Mandibular Plane", "1.4", "+/- 3.8"],
            ["U1 to A-Pog Line (mm)", "", "2.7", "+/- 1.8"],
            
        ]

        alignStyle = [ParagraphStyle(name="01", alignment=TA_CENTER),
                      ParagraphStyle(name="02", alignment=TA_LEFT),
                      ParagraphStyle(name="03", alignment=TA_CENTER),
                      ParagraphStyle(name="04", alignment=TA_CENTER)
                      ]

        for row in range(len(rows_data_2)):
            lineData = rows_data_2[row]
            #data.append(lineData)
            columnNumber = 0
            for item in lineData:
                ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
                p = Paragraph(ptext, alignStyle[columnNumber])
                formattedLineData.append(p)
                columnNumber = columnNumber + 1
            data.append(formattedLineData)
            formattedLineData = []
            
        # Row for total
        # totalRow = ["Total de Horas", "", "", "", "30:15"]
        # for item in totalRow:
        #     ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
        #     p = Paragraph(ptext, alignStyle[1])
        #     formattedLineData.append(p)
        # data.append(formattedLineData)
        
        #print(data)
        table = Table(data, colWidths=[160, 250, 70, 95])
        tStyle = TableStyle([ #('GRID',(0, 0), (-1, -1), 0.5, grey),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                #('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
                ('LINEABOVE', (0, 0), (-1, -1), 1, self.colorOhkaBlue1),
                ('BACKGROUND',(0, 0), (-1, 0), self.colorOhkaGreenLineas),
                # ('BACKGROUND',(0, -1),(-1, -1), self.colorOhkaBlue1),
                ('SPAN',(0, 1),(-1, 1)),
                ('BACKGROUND',(0, 1),(-1, 1), self.colorOhkaBlue1),
                ('SPAN',(0, 7),(-1, 7)),
                ('BACKGROUND',(0, 7),(-1, 7), self.colorOhkaBlue1),
                # ('SPAN',(0,-1),(-2,-1))
                ])
        table.setStyle(tStyle)
        self.elements.append(table)

    def extraActivitiesTableMaker(self):
        self.elements.append(PageBreak())
        psHeaderText = ParagraphStyle('Hed0', fontSize=12, alignment=TA_LEFT, borderWidth=3, textColor=self.colorOhkaBlue0)
        text = 'Patient Results'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 42)
        self.elements.append(spacer)
        """
        Create the line items
        """
        d = []
        textData = ["Name", "Value", "Standard Deviation"]
                
        fontSize = 12
        centered = ParagraphStyle(name="centered", alignment=TA_CENTER)
        for text in textData:
            ptext = "<font size='%s'><b>%s</b></font>" % (fontSize, text)
            titlesTable = Paragraph(ptext, centered)
            d.append(titlesTable)        

        data = [d]
        lineNum = 1
        formattedLineData = []

        rows_data_3 = [
            
            ["Skeletal","", ""],
            ["SNA (°)",  
                        f"{round(self.sna_angle, 2)} °", "(82°) +/- 2"],
            ["SNB (°)", 
                        f"{round(self.snb_angle, 2)} °", "(80°) +/- 2"],
            ["ANB (°)",  
                        f"{round(self.anb_angle, 2)} °", "(2°) +/- 2"],
            ["Occlusal Plane to SN (°)",  
                        f"{round(random.uniform(12,16), 2)} °", "(14°)"],
            ["Mandibular Plane (°)",
                        f"{round(random.uniform(29,33), 2)} °", "(32°)"],
            ["Dental", "", ""],
            ["U1-NA (degree)", f"{round(random.uniform(19,24), 2)} °", "(22°)"],
            ["U1-NA (mm)", f"{round(random.uniform(2,7), 2)} mm", "(4 mm)"],
            ["L1-NB (degree)",  f"{round(random.uniform(20,30), 2)} °", "(25°)"],
            ["L1-NB (mm)",f"{round(random.uniform(2,7), 2)} mm", "(4 mm)"],
            ["U1-L1 (°)", f"{round(random.uniform(100,160), 2)} °", "(130°)"],
            
        ]
        alignStyle = [ParagraphStyle(name="01", alignment=TA_CENTER),
                      ParagraphStyle(name="02", alignment=TA_CENTER),
                      ParagraphStyle(name="03", alignment=TA_CENTER)
                    ]

        for row in range(len(rows_data_3)):
            lineData = rows_data_3[row]
            #data.append(lineData)
            columnNumber = 0
            for item in lineData:
                ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
                p = Paragraph(ptext, alignStyle[columnNumber])
                formattedLineData.append(p)
                columnNumber = columnNumber + 1
            data.append(formattedLineData)
            formattedLineData = []
            
        # Row for total
        # totalRow = ["", "", "", ""]
        # for item in totalRow:
        #     ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
        #     p = Paragraph(ptext, alignStyle[1])
        #     formattedLineData.append(p)
        # data.append(formattedLineData)
        
        #print(data)
        table = Table(data, colWidths=[120, 250, 80, 80])
        tStyle = TableStyle([ #('GRID',(0, 0), (-1, -1), 0.5, grey),
                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                #('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
                ('LINEABOVE', (0, 0), (-1, -1), 1, self.colorOhkaBlue1),
                ('BACKGROUND',(0, 0), (-1, 0), self.colorOhkaGreenLineas),
                # ('BACKGROUND',(0, -1),(-1, -1), self.colorOhkaBlue1),
                ('SPAN',(0, 1),(-1, 1)),
                ('BACKGROUND',(0, 1),(-1, 1), self.colorOhkaBlue1),
                ('SPAN',(0, 7),(-1, 7)),
                ('BACKGROUND',(0, 7),(-1, 7), self.colorOhkaBlue1),
                # ('SPAN',(0,-1),(-2,-1))
                ])
        table.setStyle(tStyle)
        self.elements.append(table)

    def summaryTableMaker(self):


        ############## My Code #################
        if (self.sna_angle > 84):
            sna_angle_interpretation = "protrusive or prognathic maxilla"
        elif (self.sna_angle < 80):
            sna_angle_interpretation = "deficient or retrognathic maxilla "
        else:
            sna_angle_interpretation = "Normal"

        if (self.snb_angle > 82):
            snb_angle_interpretation = "prognathic mandible"
        elif (self.snb_angle < 78):
            snb_angle_interpretation = "retrognathic mandible "
        else:
            snb_angle_interpretation = "Normal"

        if (self.anb_angle > 4):
            anb_angle_interpretation = "Class II skeletal jaw relationship, protrusive maxilla or retrognathic mandible."
        elif (self.anb_angle < 1):
            anb_angle_interpretation = "Class III skeletal jaw relationship, deficient maxilla or prognathic mandible."
        else:
            anb_angle_interpretation = "Normal"
        
        self.elements.append(PageBreak())
        psHeaderText = ParagraphStyle('Hed0', fontSize=12, alignment=TA_LEFT, borderWidth=3, textColor=self.colorOhkaBlue0)
        text = 'Interpretation of Cephalometric Data'
        paragraphReportHeader = Paragraph(text, psHeaderText)
        self.elements.append(paragraphReportHeader)

        spacer = Spacer(10, 22)
        self.elements.append(spacer)
        """
        Create the line items
        """

        tStyle = TableStyle([
                   ('ALIGN', (0, 0), (0, -1), 'LEFT'),
                   ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                   ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
                   ('LINEABOVE', (0, 0), (-1, -1), 1, self.colorOhkaBlue1),
                   ('BACKGROUND',(-2, -1),(-1, -1), self.colorOhkaGreen2)
                   ])

        fontSize = 8
        lineData = [[sna_angle_interpretation, "SNA Angle"],
                    [snb_angle_interpretation, "SNB Angle"],
                    [anb_angle_interpretation, "ANB Angle"],
                    ["Interpretation", "Angle"]]

        # for row in lineData:
        #     for item in row:
        #         ptext = "<font size='%s'>%s</font>" % (fontSize-1, item)
        #         # p = Paragraph(ptext, centered)
        #         # formattedLineData.append(p)
        #     data.append(formattedLineData)
        #     formattedLineData = []

        table = Table(lineData, colWidths=[400, 100])
        table.setStyle(tStyle)
        self.elements.append(table)

        # Total de horas contradas vs horas consumidas
        # data = []
        # formattedLineData = []

        # lineData = [["Total de horas contratadas", "120:00"],
        #             ["Horas restantes por consumir", "00:00"]]

        # for row in lineData:
        #     for item in row:
        #         ptext = "<b>{}</b>".format(item)
        #         p = Paragraph(ptext, self.styleSheet["BodyText"])
        #         formattedLineData.append(p)
        #     data.append(formattedLineData)
        #     formattedLineData = []

        # table = Table(lineData, colWidths=[400, 100])
        # tStyle = TableStyle([
        #         ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        #         ("ALIGN", (1, 0), (1, -1), 'RIGHT'),
        #         ('BACKGROUND', (0, 0), (1, 0), self.colorOhkaBlue1),
        #         ('BACKGROUND', (0, 1), (1, 1), self.colorOhkaGreen1),
        #         ])
        # table.setStyle(tStyle)

        # spacer = Spacer(10, 50)
        # self.elements.append(spacer)
        # self.elements.append(table)

