fetch("job_queue.json")
  .then(res => res.json())
  .then(jobs => {
    const container = document.getElementById("jobList");
    jobs.forEach(job => {
      const card = document.createElement("div");
      card.className = "job-card";
      card.innerHTML = `
        <h3>${job.title}</h3>
        <p>${job.company}</p>
        <p><a href="${job.link}" target="_blank">Apply Link</a></p>
        <p>Match Score: ${job.match_score || "N/A"}</p>
      `;
      container.appendChild(card);
    });
  });