
main :- write('\nWelcome! This is flight management system!\n').
/*Data Regarding Different flights*/
flight(toronto,aircanada,london,550,420).
flight(toronto,united,london,700,480).
flight(toronto,united,madrid,1000,600).
flight(toronto,ibeira,madrid,850,540).
flight(toronto,aircanada,madrid,950,540).

flight(london,aircanada,toronto,575,440).
flight(london,united,toronto,725,500).
flight(london,ibeira,barcelona,295,320).

flight(barcelona,ibeira,london,260,270).
flight(barcelona,ibeira, valencia,150,105).
flight(barcelona,ibeira, madrid,160,95).
flight(barcelona,aircanada,madrid,140,90).

flight(madrid, aircanada, barcelona, 175, 105).
flight(madrid, ibeira, barcelona, 205, 110).
flight(madrid, ibeira, valencia, 115, 95).
flight(madrid, ibeira, malaga, 125, 105).
flight(madrid, ibeira, toronto, 875, 525).
flight(madrid, united, toronto, 1025, 585).
flight(madrid, aircanada, toronto, 975, 525).

flight(valencia, ibeira, barcelona, 150, 95).
flight(valencia, ibeira, madrid, 80, 70).
flight(valencia, ibeira, malaga, 120, 140).

flight(malaga, ibeira, valencia, 130, 150).
flight(malaga, ibeira, madrid, 100, 90).

flight(paris, united, toulouse, 85, 180).

flight(toulouse, united, paris, 75, 150).

/*Airport data*/
airport(toronto, 50, 60).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).
airport(paris, 50, 60).
airport(toulouse, 40, 30).
airport(london, 75, 80).

printflights(City1, City2) :-
	(flight(City1,Plane,City2,Price,Dur) ; flight(City2,Plane,City1,Price,Dur)),
	printflight(City1,Plane,City2,Price,Dur) , printflight(City2,Plane,City1,Price,Dur).

printflight(City1,Plane,City2,Price,Dur):-
	write('Flight name\n'),
	write(Plane),
	write('\nDeparture from\n'),
	write(City1),
	write('\nLanding On\n'),
	write(City2),
	write('\nFare of journey\n'),
	write(Price),
	write('\nJourney Duration\n'),
	write(Dur),
	write('\n').
/*Is there a flight from toronto to madrid ?*/
is_flight_from_x_to_y(X, Y) :- 
		(flight(X, Plane, Y, Price, Dur); 
		flight(Y, Plane, X, Price, Dur)).		
/*If the price of flight is < 400 from city A to city B then it is cheap*/
is_cheap(A, C, B):-
	(flight(A,C,B,Price,Dur);
	flight(B,C,A,Price,Dur)),
	(Price < 400 ).
/*Is it possible to go from Toronto to paris in 2 flights ?*/
is_possible_from_x_to_y_intwo_flight(A, B):-
	(is_flight_from_x_to_y(A, C), is_flight_from_x_to_y(C, B));
	(is_flight_from_x_to_y(B, C), is_flight_from_x_to_y(C, A)).	 

/*A flight is preffered if is it either cheap or its with aircanada*/
is_preferred(A, C, B) :-
	is_cheap(A,C,B);
	((C = aircanada) ,(flight(A,aircanada,B,D,E) ; flight(B,aircanada,A,D,E))) .


                                                                                                                                                                                    










