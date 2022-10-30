import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Opeyemi Peter Ojajuni, Ph.D.
##### *Resume* 
''')

image = Image.open('jaju.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Experienced Network Engineer, Researcher and Educator with almost ten years of experience in digital transformation and I am passionate about technology and human development. 
- Looking for opportunities where data and technology can be used to provide insights for decision-making to empower individuals and organizations to address business and social issues.
- I possess strong programming skills in Python, am a certified IBM AI practitioner, have delivered Full Stack Data Science projects, am a Cisco Certified Network Associate (CCNA), and am a certified AWS Cloud Practitioner.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #696969;">
  <a class="navbar-brand" href="https://jajupeter.webflow.io/" target="_blank">O.P.O </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Doctor of Philosophy** (Science and Mathematics Educatio), *Southern University and A&M College, Baton Rouge, Louisiana*, USA', '2018-2023')
st.markdown('''
- GPA: `3.78`
- Research thesis entitled `Increasing students Computational Thinking skill levels using Virtual Reality (VR) in cybersecurity-additive manufacturing training`.
- Winner - 2020 DXC/SUBR Cloud computing Virtual Camp Team Project Competition.
- Runner up - Best Oral Presentation at 76th Joint Meeting of BKX and NIS, Beta Kappa Chi and National Institute of Science, March 28-30, 2019 - Atlanta, GA..
''')

txt('**Masters of Science** (Mobile and Satellite Communication), *University of Surrey*, UK',
'2013-2014')
st.markdown('''
- GPA: `3.3`
''')

txt('**Bachelors of Engineering** (Computer Engineering), *Covenant University Ota*, Nigeria',
'2007-2012')
st.markdown('''
- GPA: `3.8`
''')
#####################
st.markdown('''
## Work Experience
''')

txt('**GRADUATE RESEARCH ASSISTANT**, Southern University and A&M College, Baton Rouge, Louisiana',
'2018-present')
st.markdown('''
- Evaluated the impact of immersive technology on the development of problem-solving skills by using `quantitative and qualitative research design`. 
- Used the following statistical analysis - `Factor analysis, internal consistency, and test re-test reliability` test to analyze the relationship between immersive technology and computational thinking skill development in STEM students.
- Collected observational data to provide insight on students attitude and perception towards the use of immersive technology in engineering education.
- Designed and created immersive virtual reality education applications using `Unity Game engine` to foster problem-solving skills, student engagement and motivation in cybersecurity- additive manufacturing training. 
- Provided mentorship and supervision to `3` graduate students working on AI/Machine Learning projects that received IBM Masters Fellowship.
- Peer reviewed `100+` research articles for leading scientific journals.
''')

st.markdown('''
  `Research topic: Enhancing Additive Manufacturing Education with Virtual Reality.`
- Collaborated with the faculty members to design virtual reality training modules to foster additive manufacturing and cybersecurity education.
- Analyzed the impact of Virtual Reality (VR) and Artificial intelligence (AI) on skill acquisition and retention.
- Collaborated with faculty member to simulate a virtual process of additive manufacturing.
''')
st.markdown('''
  `Research topic: Predicting Student Academic Performance Using Machine Learning.`
- Applied machine learning models to predict students' academic performance.
- Developed an accurate model by comparing several Machine Learning models with Deep Learning models.
- Utilized feature engineering to investigate the factors affecting student academic performance.
- Published research finding in an international conference on computational science and its applications.
''')
st.markdown('''
  `Research topic: Analysis of an Automobile Driver Drowsiness Detection Technique Based on Facial Features Using Machine Learning.`
- Analyzed the pros and cons of drowsiness detection classification approaches in terms of performance.
- Compared the performance of Machine Learning classifiers to Deep Learning in classifying drowsiness. 
- Utilized the OpenCV library in Computer Vision to detect faces and classify drowsiness.
- Used `Haar Cascade classifiers` and `Dlib library` to extract facial features. 
''')
st.markdown('''
  `Research topic: Distributed Denial-of-Service Attack Detection and Mitigation for the Internet of Things (IoT) networks.`
- Implemented a `Software Defined Network (SDN)` Framework to detect and mitigate cyber-attacks on internet of thing (IoT) infrastructure using a policy-based approach.
- Explored the programmable networking functionality of the SDN controller by writing JavaScript to detect and mitigate DDoS attacks.
- Evaluated and compared the SDN framework's capability to an existing framework in terms of network throughput and network latency performance metrics to analyze Internet network traffic in real-time.
- Published research finding in International Journal of Technology Diffusion. 
''')

txt('**DATA SCIENCE AND ARTIFICIAL INTELLIGENCE ENGINEER**, IBM Data Science Academy',
'2021')
st.markdown('''
- Collected data that shows fraud indicators using IBM Visual Recognition 
- Prepared a training data set with the fraud indicators
- Trained a fraud prediction model using IBM Watson Studio
- Deployed the model for use in the fraud triaging app using IBM Watson Studio.
''')

txt('**BUSINESS ANALYST/CLOUD ENGINEER**, 2020 DXC/SUBR Cloud computing Virtual Camp',
'2020')
st.markdown('''
- Led a 6-member cross-functional team that evaluated the challenges associated with the architecture of a company's access database.
- Recommended a new solution to address the problem of the access database architecture by migrating the database to the cloud and redesigning the database to track customers and categorize data.
- Designed and implemented the migration from on-site access databases to `Azure cloud services`.
- Assessed the potential risks associated with the use of the recommended solution.
''')

txt('**IT CONSULTANT/ IT INSTRUCTOR**, Hacey, Lagos Nigeria',
'2018- Present')
st.markdown('''
- Reduced operational expenditures by `30%` by recommending a secure IT core infrastructure after analyzing and evaluating the company's IT infrastructure.
- Increased revenue by `40%` by recommending data visualization applications like `Tableau & Power BI` to meet clients requirements. 
- Developed `instructional design` to close the digital gender gap and promote digital inclusion of young women in STEM field. 
- Served on a cross-functional team to train over 300 young women in tertiary institutions on digital skills to design solutions that support the sustainable development goals. 
- Organized research colloquia and seminars to raise awareness of the importance of improving digital skills among minority groups in the STEM field. 
''')

txt('**SENIOR NETWORK ENGINEER**, EKO Electricity Distribution Company, Lagos Nigeria',
'3/2018 - 6/2018')
st.markdown('''
- Administered `Office 365, Microsoft Exchange Server, Cyberoam Firewall, and Active Directory`.
- Attained network availability of `99.999%` by revamping the `LAN network infrastructure` and installing `PRTG` for network monitoring.
- Improved the companys network security by `60%` by redesigning the networks Internet Protocol (IP) address scheme and implementing `WPA2-Enterprise authentication`. 
''')

txt('**SENIOR NETWORK ENGINEER**, Staunton & Lycett, Abuja, Nigeria',
'2015 - 2018')
st.markdown('''
- Managed a 7-member team to design and implement campus wireless external network through efficient `2ghz and 5ghz Wi-Fi planning` with `99.998%` uptime availability.
- Increased user access speed to over `100%` by designing and deploying a double-redundant secured network core infrastructure.
- Reduced capital expenditures by `50%` by configuring scalable virtual servers for the software development team to host student software applications.
- Reduce capital expenditures by `50%` by migrating some application servers to the cloud.
- Led a 6-member cross-functional team to design and install scalable digital communication network, and IP surveillance system in 3 colleges. 
- Collaborated with the software development team in the implementation of a Learning Management System to facilitate the adoption of blended learning which increase student performance by `40%`. 
''')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`, `Linux`, `JavaScript(intermediate`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`, `PyTorch`, `IBM Watson Studio`, `JupyterLab`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Network Infrastructure ', '`TCP/IP`, `DHCP`, `DNS`,`NAT`, `BGP`, `OSPF`, `VLANs`, `IPsec VPN`, `Route 53`, `WiFi802.11ac`')
txt3('Cloud Computing ', '`AWS`, `Azure`, `IAM`,`S3`, `EC2`, `Route53`, `GCP`')
txt3('Model deployment', '`streamlit`,  `AWS`, `Git`')
txt3('Project management', '`Agile-scrum`,  `Asana`, `Jira`, `Slack`')
txt3('Process improvement', '`Process Mapping `, `Use case`, `User Story`')
txt3('Research Designs ', '`Quantitative, `, `Qualitative`, `Mixed-method`, `A/B testing`, `hypothesis testing`')



#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/opeyemi-ojajuni-78419283/')
txt2('GitHub', 'https://github.com/jajupeter')
txt2('ORCID', 'https://orcid.org/0000-0002-4294-2528')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Opeyemi-Ojajuni')

