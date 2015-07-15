# -*- coding:utf-8 -*-
import sys
import csv

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

def cardParse(card):
    c = CardClass();
    lines = card.split("\n");
    for line in lines:
        if line.startswith("N:"):
            c.N = line[2:len(line) - 1];
            continue;
        if line.startswith("FN:"):
            c.FN = line[3:len(line) - 1];
            continue;
        if line.startswith("TEL;"):
            c.TEL += line[4:len(line) - 1] + ",";
            continue;
        c.OTHER += line + "\n";
    return c;

if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = open(sys.argv[1], "r");
        writer = csv.writer(file(sys.argv[1]+".csv", 'wb'));
        linecount = 0;
        cardstr = "";
        while True:
            line = f.readline();
            if line:
                if line.startswith("BEGIN:VCARD"):
                    cardstr = "";
                else:
                    if line.startswith("END:VCARD"):
                        card = cardParse(cardstr);
                        csvline = card.toCsvLine();
                        csvline = csvline.decode("utf-8");
                        writer.writerow(csvline);
                        cardstr = "";
                    else:
                        line = line.replace("\r", "");
                        line = line.replace("\n", "");
                        cardstr = cardstr + line + "\n";
                linecount += 1;
            else:
                break;
        f.close();
    else:
        print "vcf2csv xxx.vcf";
