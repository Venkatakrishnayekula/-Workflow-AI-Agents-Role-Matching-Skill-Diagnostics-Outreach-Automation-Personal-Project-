from generate_docs import generate_resume

sample_profile = {
    "skills": "spring boot, react, docker, kubernetes, oauth, aws"
}

job_keywords = {
    "backend": ["spring boot", "rest api", "microservices", "oauth", "jwt", "jpa", "azure", "aws"],
    "frontend": ["react", "angular", "redux", "responsive design", "hooks"],
    "devops": ["jenkins", "docker", "kubernetes", "terraform", "ci/cd"],
    "cloud": ["azure devops", "aks", "aws ec2", "cloudwatch"]
}

generate_resume(sample_profile, job_keywords)
print("✅ Resume generated successfully.")