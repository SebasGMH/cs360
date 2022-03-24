/*Giuliani Martinez
cs360
9/27/21
HW#1

Program records data on code
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(){
    //set variables to store info
    vector<string> functionNames, returnType, variableName, variableValue, variableType;

    //keep track of open brackets to define functions
    int openBr = 0;
    
    //new place to star reading after pushback
    int nstart = 0;
    
    //opens and reads file
    string text_file, cline,cover;
    cin >> text_file;
    ifstream infile (text_file);
    //test if file can be read
    if(infile.is_open()){
        //flag for when file is over
        while(!infile.eof()){
            getline(infile,cline);
            if (openBr == 0){
            //retrieve return type
            for(int x=0; x < cline.size(); x++){
                if (cline[x] == 'i'){
                    cover = "int";
                    returnType.push_back(cover);
                    cover = "";
                    nstart = 4;
                    break;
                }
                if (cline[x] == 'v'){
                    cover = "void";
                    returnType.push_back(cover);
                    cover = "";
                    nstart = 5;
                    break;
                }
            }
            //retrieve function names
            for(int x=nstart; x < cline.size(); x++){
                if (cline[x] == '('){
                    functionNames.push_back(cover);
                    cover = "";
                    break;
                }
                cover = cover + cline[x];
            }
            //update bracket counter- overkill in this step
                for(int x=0; x < cline.size(); x++){
                    if (cline[x] == '{') openBr = openBr + 1;
                    if (cline[x] == '}') openBr = openBr - 1;
                }
            cline = "";
            nstart = 0;
            }
            //info for things inside function
            else if (openBr != 0){
                //update bracket counter
                for(int x=0; x < cline.size(); x++){
                    if (cline[x] == '{') openBr = openBr + 1;
                    if (cline[x] == '}') openBr = openBr - 1;
                }
                //var type cases
                for(int x=0; x < cline.size(); x++){
                    if(cline[x] == 'i')
                    cover = "int";
                    if (cover == "int" && cline[5] == '['){
                        variableType.push_back("array");
                        cover = "";
                        nstart = x + 4;
                    }
                    if (cover == "int" && cline[x+5] == '='){
                        variableType.push_back(cover);
                        cover = "";
                        nstart = x + 4; 
                    }
                }
                //retrieve var names
                for(int x=nstart; x < cline.size(); x++){
                    if (cline[x+1] == '['&& cline[x+4] == '='){
                        cover = cline[x];
                        variableName.push_back(cover);
                        cover = "";
                    }
                    if (cline[x+1] == '='&& cline[x] != ']'){
                        cover = cline[x];
                        variableName.push_back(cover);
                        cover = "";
                    }
                }
                //retrieve var values
                for(int x=nstart; x < cline.size(); x++){
                    if (cline[x] == '='){
                        for(int i=x+1; i < cline.size(); i++){
                            if (cline[i] == ';') break;
                            cover = cover + cline[i];
                            if (cline[x+2] == ',') break;
                        }
                        variableValue.push_back(cover);
                        cover = "";
                    }
                }
                cline = "";
                nstart = 0;
            }
        }

        infile.close();
    }
    else cout << "no file" << endl;

    cout << "function names: ";
    for (int x=0; x < functionNames.size(); x++)
        cout << functionNames[x] << " ";

    cout << "\nreturn types: ";
    for (int x=0; x < returnType.size(); x++)
        cout << returnType[x] << " ";

    cout << "\nvariable names: ";
    for (int x=0; x < variableName.size(); x++)
        cout << variableName[x] << " ";

    cout << "\nvariable values: ";
    for (int x=0; x < variableValue.size(); x++)
        cout << variableValue[x] << " ";

    cout << "\nvariable types: ";
    for (int x=0; x < variableType.size(); x++)
        cout << variableType[x] << " ";
    cout << endl;

    return 0;
}