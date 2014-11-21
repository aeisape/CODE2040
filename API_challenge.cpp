/**CODE2040 API challenge
   Adebayo Eisape
   email: aeisape1@jhu.edu
*/

#include <algorithm>
#include <iostream>
#include <json/json.h>
#include <string>
#include <assert.h>

using std::string;

/**
retrieve json?
*/
string get_jason(string address) {
    //get jason from internets
    string jason; //= something or other

    return jason;
}

/**
get stgring to reverse
*/
string get_revstr(string jason) {
    //convert to string?
    string str;


    return str;
}

/**
reverse the string
*/
void reverse_string(string & revstr) {
    //reverse string
    std::reverse(revstr.begin(), revstr.end());

    //convert to json?


    //send it on its way


}

/**
needle in a haystack
*/
//compare function for sort
bool cmp(string a, string b) {
    return( a < b);
}

//retrieve needle
string get_needle(string jason) {

    //nnedle container
    string needle;

    //get needle from json whatever

    return needle;
}

//retrieve haystack
std::vector<string> get_haystack(string jason) {

    //haybale (for transporting haystack)
    std::vector<string> haystack;

    //get haystack from json whatever


    return haystack;
}

//find needle in haystack
int find_needle(string needle, std::vector<string> haystack) {

    //sort haystack --(O(NlogN)); array needs to be sorted in order to use find
    std::sort(haystack.begin(), haystack.end(), cmp);

    //find returns a reference to the specified value(needle) in the given
    //vector(haystack). '.begin()' returns a reference to the beginning of the the vector;
    //using pointer arithmetic we can find the distance between the two in the
    //haystack which will be the same as the position of the found postion (needle).
    int index = std::find(haystack.begin(), haystack.end(), needle) - haystack.begin();

    //convert to json??


    //send it on its way..

    //return index for testing purposes
    return index;
}

/**
prefixes - given a prefix and an array of strings,
remove all strings containin that prefix
*/
string get_prefix(string jason) {
    string prefix;

    //get prfix from jason whatever


    return prefix;
}



std::vector<string> get_array() {
    std::vector<string> _array;

    //get array from jason whatever


    return _array;
}

//remove words containing the given prefix from the given array, using parallel arrays
void remove_w_prefixes(string prefix, std::vector<string> & _array) {
    std::sort(_array.begin(), _array.end(), cmp);

    int i = 0;
    while (_array[i][0] != prefix[0]){
        i++;
    }

    bool broke = false;
    while(_array[i][0] == prefix[0]){
        for(unsigned int j = 0; j < prefix.length(); j++){
            if (prefix[j] != _array[i][j]){
            broke = true;
            break;
            }
        }
        if(broke == false)
        //remove ith entry
            _array.erase(_array.begin()+i);
        else {
            i++;
            broke = false;
        }
    }
}

/**
test for reverse_string()
*/
void test_reverse_string() {
    std::cout<<"====================="<<std::endl;
    std::cout<<"Testing reverse_string()"<<std::endl;

    //momma's name!
    string str = "Bashira Musa";

    //print to check
    std::cout<<str<<std::endl;

    //reverse string #shocking
    reverse_string(str);

    //if string is reversed continue, else, terminate
    assert(str == "asuM arihsaB");

    //print reversed string
    std::cout<<str<<std::endl;

    //self gratification
    std::cout<<"reverse string test passed"<<std::endl;
    std::cout<<std::endl;

    std::cout<<"once more, with a palendrome"<<std::endl;
    str = "Racecar";
    std::cout<<str<<std::endl;
    reverse_string(str);
    std::cout<<str<<std::endl;
}

/**
test for find_needle in a haystack()
*/
void test_find_needle() {
    std::cout<<"====================="<<std::endl;
    std::cout<<"Testing find_needle()"<<std::endl;

    //create a needle to look for
    string needle = "derp";

    //tell the world about the needle
    std::cout<<"needle: "<<needle<<std::endl;

    //create a haystack of "random" strings //derp is at position 7
    std::vector<string> haystack = {"CODE2040", "API", "Challenge", "Documentation", "Thanks", "for", "derp", "completing", "the", "CODE2040", "enrollment"};

    //get location f needle in haystack
    int loc = find_needle(needle, haystack);

    //check if index of derp is 7, abort otherwise
    assert(loc == 7);

    //print position of needle in haystack
    std::cout<<"I FOUND THE NEEDLE!!! It's at position "<<loc<<std::endl;

    //self gratification
    std::cout<<"needle in haystack test passed"<<std::endl;
}

/**
test for remove_w_prefixes()
*/
void test_w_pre() {
    string prefix = "pre";

    std::vector<string> ra = {"Never", "preconnected",  "to", "API","prebefore", "?", "You" ,"precan", "do", "this" ,"!", "preWe’ll" ,"walk", "preyou", "through", "how", "to", "think", "about", "prethe", "problem", "and", "preprovide","some", "tips","on", "how", "to" ,"find", "advice", "."};
    unsigned int i;
    for(i = 0; i<ra.size(); i++){
        std::cout<<ra[i]<<" ";
    }
    std::cout<<std::endl;

    remove_w_prefixes(prefix, ra);

    for(i = 0; i<ra.size(); i++){
        std::cout<<ra[i]<<" ";
    }

}

/**
run all tests
*/
void full_test_battery() {

    test_reverse_string();
    std::cout<<std::endl;

    test_find_needle();
    std::cout<<std::endl;

    test_w_pre();
    std::cout<<std::endl;

    std::cout<<"\n\t\tAll tests passed!"<<std::endl;
    std::cout<<"\t\t'Aal iz well'"<<std::endl;
}


int main() {
    full_test_battery();

}

