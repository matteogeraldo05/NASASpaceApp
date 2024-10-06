#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std;

class DataPoint {
    private:
        string year;
        string month;
        string day;
        string hour;
        string minute;
        string second;
        string relTime;
        string velocity;
        string LTA;
        string STA;

    public:
        // Constructors
        DataPoint() {
            year = "0";
            month = "0";
            day = "0";
            hour = "0";
            minute = "0";
            second = "0";
            relTime = "0";
            velocity = "0";
            LTA = "0";
            STA = "0";
        }

        DataPoint(string sYear, string sMonth, string sDay, string sHour, string sMinute, string sSecond, string sRelTime, string sVelocity, string sLTA, string sSTA) {
            this->year = sYear;
            this->month = sMonth;
            this->day = sDay;
            this->hour = sHour;
            this->minute = sMinute;
            this->second = sSecond;
            this->relTime = sRelTime;
            this->velocity = sVelocity;
            this->LTA = sLTA;
            this->STA = sSTA;

        }

        // Getters and Setters
        string getRelTime() const {
            return relTime;
        }

        void setRelTime(string relTime) {
            this->relTime = relTime;
        }

        string getVelocity() const {
            return velocity;
        }

        void setVelocity(string velocity) {
            this->velocity = velocity;
        }

        string getLTA() const {
            return LTA;
        }

        void setLTA(string LTA) {
            this->LTA = LTA;
        }

        string getSTA() const {
            return STA;
        }

        void setSTA(string STA) {
            this->STA = STA;
        }

        string getYear() const {
            return year;
        }

        void setYear(string year) {
            this->year = year;
        }

        string getMonth() const {
            return month;
        }

        void setMonth(string month) {
            this->month = month;
        }

        string getDay() const {
            return day;
        }

        void setDay(string day) {
            this->day = day;
        }

        string getHour() const {
            return hour;
        }

        void setHour(string hour) {
            this->hour = hour;
        }

        string getMinute() const {
            return minute;
        }

        void setMinute(string minute) {
            this->minute = minute;
        }

        string getSecond() const {
            return second;
        }

        void setSecond(string second) {
            this->second = second;
        }


        void toString(){
            cout << year << "-" << month << "-" << day << " | " << hour << ":" << minute << ":" << second << " | "<< "Relative Time: " << relTime << " | Velocity(c/s): " << velocity << endl;
        }

};


string substringAfter(const std::string& str, size_t startIndex, char lookFor) {
    // Find the first comma after the specified index
    size_t commaPos = str.find(lookFor, startIndex);
    
    // Check if a comma was found
    if (commaPos != std::string::npos) {
        // Return the substring after the comma
        return str.substr(commaPos + 1);
    }
    
    // If no comma is found, return an empty string or handle accordingly
    return ""; 
}

string substringBefore(const std::string& str, size_t startIndex, char lookFor) {
    // Find the first comma after the specified index
    size_t commaPos = str.find(lookFor, startIndex);
    
    // Check if a comma was found
    if (commaPos != std::string::npos) {
        // Return the substring after the comma
        return str.substr(0, commaPos);
    }
    
    // If no comma is found, return an empty string or handle accordingly
    return ""; 
}

string substringBetween(const std::string& str, size_t startIndex, char lookFor) {
    // Find the first comma after the specified index
    size_t commaPos = str.find(lookFor, startIndex);
    
    // Check if a comma was found
    if (commaPos != std::string::npos) {
        // Return the substring after the comma
        return str.substr(startIndex, commaPos);
    }
    
    // If no comma is found, return an empty string or handle accordingly
    return ""; 
}




int main() {
    string myText;

    list<DataPoint> listOfPoints;

    ifstream MyReadFile("XB.ELYSE.02.BHV.2022-01-02HR04_evid0006.csv");

    if (MyReadFile.is_open()) {
        int lineNum = 0;
        while (getline(MyReadFile, myText)) {
            if (lineNum != 0){

                string year = substringBefore(myText,0,'-');
                myText = substringAfter(myText,0,'-');
                string month = substringBetween(myText, 0, '-');
                myText = substringAfter(myText,0,'-');
                string day = substringBetween(myText,0,'T');
                myText = substringAfter(myText,0,'T');
    
                string hour = substringBefore(myText,0,':');
                myText = substringAfter(myText,0,':');
                string minute = substringBetween(myText, 0, ':');
                myText = substringAfter(myText,0,':');
                string second = substringBetween(myText,0,',');
                myText = substringAfter(myText,0,',');
                

                string textBeforeComma = substringBefore(myText, 0, ',');
                myText = substringAfter(myText, 0, ',');
                string textAfterCommas = substringAfter(myText, 0, ',');
                //cout << year << "-" << month << "-" << day << " | " << hour << ":" << minute << ":" << second << " | "<< "Relative Time: " << textBeforeComma << " | Velocity(c/s): " << myText << endl;



                DataPoint point = DataPoint(year,month,day,hour,minute,second,textBeforeComma,myText, "0", "0");

                listOfPoints.push_back(point);

                point.toString();


            }
            lineNum++;
        }
        
        MyReadFile.close();
    } else {
        cout << "Unable to open file!" << endl;
    }

    return 0;
}
