# -*- coding:utf-8 -*-
import sys
import csv
import codecs

class CardClass:
    N="";
    FN="";
    TEL="";
    OTHER = "";
    def __init__(self):
        pass;
    def __del__(self):
        pass;
    def toCsvLine(self):
        return self.N+ "," + self.FN + "," + self.TEL + "," + self.OTHER;

def cardParse(cardstr):
    c = CardClass();
    lines = cardstr.split("\n");
    for line in lines:
        if line:
            if line.startswith("N:"):
                c.N = line[2:];
                continue;
            if line.startswith("FN:"):
                c.FN = line[3:];
                continue;
            if line.startswith("TEL;"):
                c.TEL += line[4:] + ",";
                continue;
            #c.OTHER += line + "\n";
    return c;

if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = open(sys.argv[1], "r");
        fw = open(sys.argv[1]+".csv", "w");
        fw.write(codecs.BOM_UTF8);
        linecount = 0;
        cardcount = 0;
        cardstr = "";
        while True:
            line = f.readline();
            if line:
                #utf8解码
                if line[:3] == codecs.BOM_UTF8:
                    line = line[3:];
                #line = line.decode("utf-8");
                if line.startswith("BEGIN:VCARD"):
                    cardstr = "";
                else:
                    if line.startswith("END:VCARD"):
                        card = cardParse(cardstr);
                        csvline = card.toCsvLine();
                        cardcount += 1;
                        print str(cardcount) + " " + csvline.decode("utf-8")
                        fw.write(csvline+"\n");
                        cardstr = "";
                    else:
                        line = line.replace("\r", "");
                        line = line.replace("\n", "");
                        cardstr = cardstr + line + "\n";
                linecount += 1;
            else:
                break;
        fw.close();
        f.close();
        print sys.argv[1] + " ok, " + str(cardcount) + "records";
    else:
        print "vcf2csv xxx.vcf";
