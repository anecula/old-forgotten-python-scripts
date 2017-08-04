__author__ = 'anecula'

import unittest

#from Kids import kids
#from Kids.kids import FaceKids as myclasstoextend
import time
import csv, os
#kids.FaceKids

os.system("assians.bat")
class Script (unittest.TestCase):

    def test_woman(self):
        #self.test = myclasstoextend.test_face(self)
        print "=============================================================================="
        print "================CSV FOR WOMEN================================"
        print "=============================================================================="
        print "=============================================================================="
        f = open("Woman/sfbtester-facedump.csv")
        csv_female = csv.reader(f)
        WFace_img = []
        WFace_Idenfified = []
        WTotal_img_founded = 0
        WMen_Face = []
        WUnknown_Face = []
        WError_Face = []
        for row in csv_female:

            if len(row) > 8:
                WFace_img.append(row[8])

                if (row[8]=="adult" and row[7]=="female"):
                     WMen_Face.append(1)

                else:
                    WMen_Face.append(0)


                if (row[8] == "unknown"):
                    WUnknown_Face.append(1)
                    WFace_Idenfified.append(0)
                else:
                    WUnknown_Face.append(0)
                    WFace_Idenfified.append(1)

                if ((row[7] == "female" and (row[8] == "unknown" or row[8] == "adult")) or (row[7]=="unknown" and row[8]=="unknown")):
                    WError_Face.append(0)
                else:
                    WError_Face.append(1)


            WTotal_img_founded = WTotal_img_founded + 1
           # print row[8]

        print zip(WFace_img, WMen_Face)
        print zip (WFace_img, WError_Face)


        Wnr_total_img = WTotal_img_founded -1
        Wnr_total_id_img = sum(WFace_Idenfified) - 1
        Wmen_face_total = sum(WMen_Face)
        Wunknown_nr = sum(WUnknown_Face)
        Werror_nr = sum(WError_Face) -1

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

if __name__ == "__main__":
    unittest.main()








