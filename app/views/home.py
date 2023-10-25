from flask import Blueprint, request, redirect, url_for, session, flash, send_file
from user_agents import parse
from urllib.parse import urlparse

from ..functions import modified_render_template, get_user_ip_address, get_geo_data
from ..forms.home import ShortenLinkForm
from ..db import ShortenLink, db, ShortenLinkTransaction
from ..config import AppConfig
from ..core_functions import generate_shorten_link, check_domain_for_banned, build_shorten_url_for
from ..limiter import limit

import json
import datetime
import qrcode
import io


home = Blueprint("Home", __name__)

# @home.route('/')
# @limit(datetime.timedelta(minutes=1), limit=30)
# def index():

#     section_data = [
#         {"title": "The New York Times", "content": "Content for The New York Times..."},
#         {"title": "The Guardian", "content": "Content for The Guardian..."},
#         {"title": "Example Newspaper 1", "content": "Content for Example Newspaper 1..."},
#         {"title": "Example Newspaper 2", "content": "Content for Example Newspaper 2..."},
#     ]
    
#     return modified_render_template(
#         "home/index.html", section_data=section_data
#     )
@home.route('/')
@limit(datetime.timedelta(minutes=1), limit=30)
def index():
    section_data = [
        {"title": "The New York Times", "content": "Content for The New York Times..."},
        {"title": "The Guardian", "content": "Content for The Guardian..."},
        {"title": "tutor", "content": "Content for Example Newspaper 1..."},
        {"title": "quran", "content": "Content for Example Newspaper 2..."},
    ]
    
    return modified_render_template(
        "home/index.html", section_data=section_data
    )



@home.route('/section/<section_title>')
def section(section_title):
    return modified_render_template("home/section.html", section_title=section_title)


@home.route('/api/course-catalog')
def course_catalog():
    # API logic for course catalog
    return "Course catalog API response"


@home.route('/api/user-reports')
def user_reports():
    # API logic for user reports
    return "User reports API response"

