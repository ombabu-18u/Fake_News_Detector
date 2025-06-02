import re
from urllib.parse import urlparse

# Configure these lists according to your needs
RELIABLE_SOURCES = ['bbc.com', 'reuters.com', 'apnews.com']
SUSPICIOUS_KEYWORDS = ['urgent', 'breaking', 'miracle cure', 'hidden truth']

def analyze_credibility(article):
    """Analyze an article and return a credibility score (0-100)"""
    score = 50  # Base score
    
    # 1. Check source reliability
    domain = article.source_url.split('/')[2] if len(article.source_url.split('/')) > 2 else article.source_url
    if 'bbc.com' in domain or 'reuters.com' in domain:  # Add your trusted sources
        score += 30
        article.source_reliability = 'Reliable'
    else:
        article.source_reliability = 'Unknown'
    
    # 2. Check for suspicious keywords
    suspicious_words = ['urgent', 'breaking', 'miracle cure']
    found_words = [word for word in suspicious_words if word in article.content.lower()]
    if found_words:
        article.keywords = ', '.join(found_words)
        score -= len(found_words) * 10
    
    # 3. Determine verification status
    article.credibility_score = max(0, min(100, score))  # Ensure score is 0-100
    
    if score > 70:
        article.verification_result = "Verified"
        article.is_verified = True
    elif score > 40:
        article.verification_result = "Pending Verification"
    else:
        article.verification_result = "Suspicious"
    
    return article