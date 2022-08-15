# Gun Violenece Archive Database

This is a current ongoing project to collect and display data regarding the gun violence in each of the US states. This is a passion project that was started and is still being maintained during my free time.

The goal of this project was to visualize gun violence incidents as they are happening in each state. It is easy to view these problems as something that doesn’t affect our lives and being able to see that these incidents are happening frequently in your state is important. Since I had started this project even, I was surprised at the frequency that these incidents were occurring. My original idea was to update the database every 3 days, however after a couple days with the script live, I realized I would need to increase the frequency. New data is being added daily with most days averaging at least 4 incidents.

To collect this data, I utilized Selenium within a Python environment. My script accesses the website and is then automated to go through each page and scrape the data. The data is then processed using Beautiful Soup and sent to my SQL server. The server is connected to tableau, which is used for data visualization, the tableau dashboard can be seen below. I have the Python script scheduled to collect data once a day and after that is done the tableau data is updated along with it.

The states shown in the map below are different shades of red depending on the number of incidents that have happened within that state. The number that is displayed on each state is the raw number of incidents that have occurred, whereas the color and ranking is per capita.

Script used to collect state population can be found here: https://github.com/noahals/state_population


<hr size="" width="" color="" >  


<div class='tableauPlaceholder' id='viz1660588564941' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Gu&#47;GunViolenceArchiveDataset&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='GunViolenceArchiveDataset&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Gu&#47;GunViolenceArchiveDataset&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div> 

https://public.tableau.com/shared/G3XJSC27Z?:display_count=n&:origin=viz_share_link
