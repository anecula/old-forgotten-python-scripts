__author__ = 'anecula'

        print "txt files for Men"
        fisier_txt("Men")
        print "txt files for Women"
        fisier_txt("Women")

        print  "txt files for Kids"
        fisier_txt("kidn")
        print "txt files for Men"
        fisier_txt("Amen")
        print "txt files for Women"
        fisier_txt("Awomen")

pushd Women
..\..\Tester_2_0_37_100\sfbtester2.exe -t -i  "..\..\..\Images\0.200\Adult-Female"
popd
pushd Men
..\..\Tester_2_0_37_100\sfbtester2.exe -t -i  "..\..\..\Images\0.200\Adult-Male"
popd


        popd
pushd kidn
..\..\Tester_2_0_37_100\sfbtester2.exe -t -i  "..\..\..\Images\0.800\Child-Female"
popd
pushd Amen
..\..\Tester_2_0_37_100\sfbtester2.exe -t -i  "..\..\..\Images\0.800\Adult-Male"
popd
pushd Awomen
..\..\Tester_2_0_37_100\sfbtester2.exe -t -i  "..\..\..\Images\0.800\Adult-Female"
popd
