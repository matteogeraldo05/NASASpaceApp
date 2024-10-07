#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <cmath> // For std::abs

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
        double velocity;
        double LTA;
        double STA;

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
            velocity = 0;
            LTA = 0;
            STA = 0;
        }

        DataPoint(string sYear, string sMonth, string sDay, string sHour, string sMinute, string sSecond, string sRelTime, double sVelocity, double sLTA, double sSTA) {
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

        double getVelocity() const {
            return velocity;
        }

        void setVelocity(double velocity) {
            this->velocity = velocity;
        }

        double getLTA() const {
            return LTA;
        }

        void setLTA(double LTA) {
            this->LTA = LTA;
        }

        double getSTA() const {
            return STA;
        }

        void setSTA(double STA) {
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
            cout << year << "-" << month << "-" << day << " | " << hour << ":" << minute << ":" << second
            << " | "<< "Relative Time: " << relTime << " | Velocity(c/s): " << velocity << " | LTA: " << this->LTA << " | STA: " << this->STA << endl;
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

double calculateLTA(vector<DataPoint*> vec, int sizeOfLTA) {
    double sum = 0;
    for (int i = 0; i < sizeOfLTA; i++) {
        sum += vec.at(i)->getVelocity();
    }

    return (sum/sizeOfLTA);

}

double calculateSTA(vector<DataPoint*> vec, int sizeOfSTA) {
    double sum = 0;
    for (int i = 0; i < sizeOfSTA; i++) {
        sum += vec.at(i)->getVelocity();
    }

    return (sum/sizeOfSTA);

}



int main() {
    string myText;

    list<DataPoint> listOfPoints;

    vector<DataPoint*> arrLTA(300, nullptr);
    vector<DataPoint*> arrSTA(30, nullptr);

    vector<DataPoint> seismicEvents;

    ifstream MyReadFile("files/perfectdata.csv");

    if (MyReadFile.is_open()) {
        int lineNum = 0;
        int sizeOfLTA = 0;
        int sizeOfSTA = 0;
        bool isSeismicEvent = false;

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
                double velocity = stod(substringAfter(myText, 0, ','));


                DataPoint point = DataPoint(year,month,day,hour,minute,second,textBeforeComma,velocity, 0, 0);
                DataPoint* newPtr = new DataPoint(year, month, day, hour, minute, second, textBeforeComma, velocity, 0, 0);


                if (sizeOfLTA < 300) {
                    arrLTA[sizeOfLTA] = newPtr; 
                    sizeOfLTA += 1;

                } else {

                    delete arrLTA[0];
                    for (int i = 0; i < 300; i++) {
                        if (i + 1 <= 300){
                            arrLTA[i] = arrLTA[i + 1];
                        }
                    }
                    arrLTA[299] = newPtr;
                }

                if (sizeOfSTA < 30) {
                    arrSTA[sizeOfSTA] = newPtr; 
                    sizeOfSTA += 1;
                } else {
                    for (int i = 0; i < 30; i++) { 
                        arrSTA[i] = arrSTA[i + 1];
                    }
                    arrSTA[29] = newPtr;
                }


                double LTA = calculateLTA(arrLTA,sizeOfLTA);
                double STA = calculateLTA(arrSTA,sizeOfSTA);
                point.setLTA(LTA);
                point.setSTA(STA);
                
                
                listOfPoints.push_back(point); 
                
                if (!(isSeismicEvent) && abs(velocity)/35 > abs(STA) && abs(STA)/35 > abs(LTA)) {
                    seismicEvents.push_back(point);
                    isSeismicEvent = true;
                }
                else if (isSeismicEvent && abs(velocity)*10 < abs(STA) && abs(STA)*10 < abs(LTA)) {
                    seismicEvents.push_back(point);
                    isSeismicEvent = false;
                }


                

            }
            lineNum++;
        }

        // for(DataPoint p : listOfPoints){
        //     p.toString();
        // }


        MyReadFile.close();
    } else {
        cout << "Unable to open file!" << endl;
    }

    cout << "----------Recorded Seismic Events:------------" << endl;

    for (int i = 0; i < seismicEvents.size(); i++) {
        if (i%2==0) {
            cout << "Start of event: " << endl;
            (seismicEvents.at(i)).toString();
        }

        else {
            cout << "End of event: "<< endl;
            (seismicEvents.at(i)).toString();
        }
    }

    return 0;
}
