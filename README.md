flick_sort
==========

Sorts your movies according to IMDB rating 


The algo :

1. Open a explorer window and let user choose
			char *getfolder(); //returns the folder address
									
      Rohan

2. Decide what to sort
			char **files(char *folder); 
  // takes folder address,
  // returns a pointer to 2d array with the file
  // names

3. Get rating (Google way) 
	  float *rate(char **filelist);
		
    anshul  Prashant


4. sort
		int *sort(float *ratingarray);
		
     anshul Chetan
			
5. create a html file with shortcuts to the files
			void output( int *sorted);									

        Prashant  Ashwani	  Rohan
