// var Enabled=true;
function posts_render(ids)
    	{
    		// if (Enabled == true)
    		// {

    		
   			$.ajax(
   			{
			    type: "GET",
			    url: "/menu_posts/",
			    data: {"sub_ch_id" : ids},

			    success: function(req)
		       {
		       	
		         $('#posts_result').html(req);

		       }
    		});
   		// }

    	}

function channel_render(ids)
{
	
   			$.ajax(
   			{
			    type: "GET",
			    url: "/channel_posts/",
			    data: {"ch_id" : ids},

			    success: function(req)
		       {
		       	
		       	// Enabled=false;
		         $('#posts_result').html(req);
		       }
    		});
}