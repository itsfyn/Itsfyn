# ItsFyn API Reference

## Overview
The ItsFyn API enables developers to integrate our privacy and security features into their applications. This document provides comprehensive documentation for all available endpoints.

## Authentication
```http
Authorization: Bearer YOUR_API_KEY
```

All API calls require authentication using your API key. Get your API key from [www.itsfyn.com/dashboard/api](https://www.itsfyn.com/dashboard/api).

## Base URL
```
https://api.itsfyn.com/v1
```

## Endpoints

### Privacy Scanner

#### Run Privacy Scan
```http
POST /scan/privacy
```

Request body:
```json
{
  "scan_type": "quick|deep|custom",
  "targets": ["email", "social", "network"],
  "depth": "low|medium|high"
}
```

Response:
```json
{
  "scan_id": "scan_123xyz",
  "status": "initiated",
  "estimated_time": 300
}
```

#### Get Scan Results
```http
GET /scan/{scan_id}/results
```

Response:
```json
{
  "scan_id": "scan_123xyz",
  "status": "completed",
  "privacy_score": 85,
  "findings": [
    {
      "type": "data_exposure",
      "severity": "high",
      "details": "Personal email found in recent breach"
    }
  ]
}
```

### Security Monitor

#### Get Security Status
```http
GET /security/status
```

Response:
```json
{
  "overall_status": "secure",
  "threats_blocked": 23,
  "last_updated": "2024-01-23T10:30:00Z",
  "active_threats": []
}
```

#### Configure Alerts
```http
POST /security/alerts/config
```

Request body:
```json
{
  "email_alerts": true,
  "push_notifications": true,
  "severity_threshold": "medium"
}
```

### Identity Protection

#### Check Digital Footprint
```http
GET /identity/footprint
```

#### Monitor Social Presence
```http
POST /identity/social/monitor
```

Request body:
```json
{
  "platforms": ["twitter", "linkedin", "facebook"],
  "keywords": ["name", "email", "phone"]
}
```

## Error Codes

| Code | Description |
|------|-------------|
| 401  | Unauthorized - Invalid API key |
| 403  | Forbidden - Insufficient permissions |
| 404  | Not Found - Resource doesn't exist |
| 429  | Too Many Requests - Rate limit exceeded |

## Rate Limits
- Free tier: 100 requests/hour
- Pro tier: 1000 requests/hour
- Enterprise tier: Custom limits

## SDKs and Libraries
- [Python SDK](https://github.com/itsfyn/python-sdk)
- [JavaScript SDK](https://github.com/itsfyn/js-sdk)
- [Java SDK](https://github.com/itsfyn/java-sdk)

## Webhooks
Configure webhooks at [www.itsfyn.com/dashboard/webhooks](https://www.itsfyn.com/dashboard/webhooks)
