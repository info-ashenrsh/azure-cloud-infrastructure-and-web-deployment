# Python logging

Example:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Application started")
logger.warning("A sample warning occurred")
logger.error("A sample operation failed")
```

Do not log submitted passwords, authorization headers, or secret environment values.
