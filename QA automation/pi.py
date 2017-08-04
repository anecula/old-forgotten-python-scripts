__author__ = 'anecula'


    def test_woman(self):
        #self.test = myclasstoextend.test_face(self)
        print "citire csv"
        print "=============================================================================="
        print "=============================================================================="
        print "=============================================================================="
        f = open("C:/Work/Classification/PyScript/Woman/sfbtester-facedump.csv")
        csv_men = csv.reader(f)
        WFace_img = []
        WFace_Idenfified = []
        WTotal_img_founded = 0
        WMen_Face = []
        WUnknown_Face = []
        WError_Face = []
        for row in csv_men:

            if len(row) > 7:
                WFace_img.append(row[7])

                if (row[7]=="female"):
                     WMen_Face.append(1)

                else:
                    WMen_Face.append(0)


                if (row[7] == "unknown"):
                    WUnknown_Face.append(1)
                    WFace_Idenfified.append(0)
                else:
                    WUnknown_Face.append(0)
                    WFace_Idenfified.append(1)

                if (row[7]!="female" or row[7]!="unknown"):
                    WError_Face.append(1)
                else:
                    WError_Face.append(0)



            WTotal_img_founded = WTotal_img_founded + 1
           # print row[8]

        print zip(WFace_img, WMen_Face)


        Wnr_total_img = WTotal_img_founded -1
        Wnr_total_id_img = sum(WFace_Idenfified) - 1
        Wmen_face_total = sum(WMen_Face)
        Wunknown_nr = sum(WUnknown_Face)
        Werror_nr = sum(WError_Face)

        print "=============================================================================="
        print "=============================================================================="
        print "Total poze"
        print Wnr_total_img

        print "Total fete identificate"
        print Wnr_total_id_img

        print "Rata de succes, poze cu barbati identificate corect"
        print Wmen_face_total

        print "Rata de poze neidentificate"
        print Wunknown_nr
        print "Rata de erori, poze de barbati identificate gresit"
        print Werror_nr

        print "=============================================================================="
        print "=============================================================================="
        print "Procent fete recunoscute din totalul de fete  "
        print "{0:.2f}%".format(float(Wnr_total_id_img)/float(Wnr_total_img) * 100)

        print "Procent fete recunoscute cu succes din totalul de fete  "

        print "{0:.2f}%".format(float(Wmen_face_total)/float(Wnr_total_img) * 100)

        print "Procent fete neidentificate din totalul de fete  "

        print "{0:.2f}%".format(float(Wunknown_nr)/float(Wnr_total_img) * 100)

        print "Procent fete recunoscute gresit din totalul de fete  "

        print "{0:.2f}%".format(float(Werror_nr)/float(Wnr_total_img) * 100)

        print "{0:.2f}%".format((float(Wmen_face_total)/float(Wnr_total_img) * 100)+(float(Wunknown_nr)/float(Wnr_total_img) * 100) +(float(Werror_nr)/float(Wnr_total_img) * 100))

        print "=============================================================================="
        print "=============================================================================="