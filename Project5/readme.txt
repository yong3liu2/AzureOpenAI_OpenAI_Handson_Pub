AI-Assisted Ski Trip planning

1. Business Objective

Current Process
Traditional Ski Trip Planning:
Researching ski resorts online or through travel agencies.
Manually comparing prices, amenities, and reviews.
Booking accommodations, transportation, lift tickets, and other activities separately.
Managing the itinerary and logistics individually.

Issues
Time consuming and human do make mistake. For example, due the complexities of managing the itinerary and logistics, a friend booked a flight which was one week off targeted dates!

Scope for this project : AI-Assisted Centralized Itinerary Management
Managing the itinerary and logistics in ski trip planning involves organizing various components:
Transportation, accommodations, 
lift tickets, activities, and schedules. 

AI can significantly aid in this area by centralizing itinerary management:
Consolidation of Information: AI can compile and manage various bookings and reservations into a single, easily accessible itinerary, reducing the hassle of juggling multiple confirmations and schedules.
Automated Updates: It can send timely reminders, updates, and suggestions for better planning and organization.

2. Data and Explore
Data sources
Booked flight itinerary
Booked car rental info
Airport parking reservation
Booked hotel accommodations
Desired activities

Explore Data
Itineraries are coming in very different forms.  There is no standard form to follow.
Might need to use different loader or tools to deal with PDF, web page, Email …

3. Architecture
Technical Services needed
Data Pipeline – Langchain loader
Data Storage - Local
LLM: Azure OpenAI
Vector Store: FAISS
User Interface: might be a web site (TBD)

4. Implementation
1) Travel itinerary loaded by Langchain loader, indexing into FAISS vector Store
2) Create Faiss retriever tool, build agent use retriever tool to grab all detailed info in each of the itineraries.
3) Create prompt message on how to-day-day activities should be planned, send the prompt into Azure OpenAI LLM to generate final Ski Trip planning report.
4) Embed ski trip requirement and final generated to-day-day activities plan into Faiss db, then use tool and agent to do the comparison, provide a score to represnt matching confidence.

5. Evaluation and Acceptance
Performance Metrics vs Baseline
Evaluation Methods
Manual
Verify all the dates info in generate daily Ski trip plan
Verify all location related info: address, contact info
Ask Ski buddies to check and see if it makes sense and accurate.

Automated
Comparison between Ski Trip plan requirement vs generated day-to-day ski plan
Provide rating (0 – not matching the requirement, 9 – best match)
Risk Assessment
PII – need to be careful on PII information retrieval. Only permitted with end user agreements.
Performance Metrics vs Baseline
It used to take a day or more, now take less then 1 hour.


6. Final comparison (auto) score is 7 out of 9.

7. Document Comparison: Compare 2 documents and high light difference 
1) "trip_report.txt" - generated day-to-day activities Ski trip report
2) "trip_planning_requirement.txt" - Ski trip planning requirement

"Please compare trip_report.txt and  trip_planning_requirement.txt and highlight the difference"

Final Answer: The differences between the trip_report.txt and trip_planning_requirement.txt files are as follows:

1. The trip_report.txt file provides a detailed day-to-day ski trip plan for a week-long Ski SLC trip, including information on departure and arrival airports, rental car pickup, hotel check-in, skiing at Solitude Mountain Resort, and dining options. The trip_planning_requirement.txt file does not contain this specific day-to-day plan.

2. The trip_report.txt file includes contact information for the Fairfield Inn & Suites Salt Lake City South hotel, such as the address and phone number. This information is not present in the trip_planning_requirement.txt file.

3. The trip_planning_requirement.txt file provides a general plan for a ski trip, including steps such as booking a flight, reserving airport parking, and packing ski gear. This information is not included in the trip_report.txt file.

Based on these differences, it seems that the trip_report.txt file provides a more detailed and specific plan for a ski trip compared to the trip_planning_requirement.txt file.


