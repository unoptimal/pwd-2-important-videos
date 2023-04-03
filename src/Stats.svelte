<script>
    export let data;

    let sortedData = [];
    sortedData = Object.values(data).sort((a, b) => b.view_count - a.view_count);
    const validData = sortedData.filter(d => !isNaN(+d.view_count));
    const average = Math.round(validData.reduce((a, b) => a + +b.view_count, 0) / validData.length);

</script>

<h2>Quick stats:</h2>
<p>Lowest video view count: {parseInt(sortedData[sortedData.length - 1].view_count).toLocaleString()} - <a href={`https://www.youtube.com/watch?v=${sortedData[sortedData.length-1].video_id}&list=PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo`}>{sortedData[sortedData.length - 1].title}</a></p>
<p>Highest video view count: {parseInt(sortedData[0].view_count).toLocaleString()} - <a href={`https://www.youtube.com/watch?v=${sortedData[0].video_id}&list=PLFsQleAWXsj_4yDeebiIADdH5FMayBiJo`}>{sortedData[0].title}</a></p>
<p>Average video view count: {average.toLocaleString()}</p>




