# Contributing to AI Hedgefund

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/ai-hedgefund.git`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Make your changes
5. Push to your branch: `git push origin feature/your-feature`
6. Submit a pull request

## Development Setup

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Running Tests

```bash
pytest tests/ -v --cov
```

## Code Style

We use:
- Black for code formatting
- isort for import sorting
- pylint for linting
- mypy for type checking

```bash
black .
isort .
pylint **/*.py
mypy .
```

## Commit Messages

Follow conventional commits:
- `feat: add new feature`
- `fix: fix bug`
- `docs: update documentation`
- `test: add tests`
- `refactor: refactor code`

## Pull Request Process

1. Ensure all tests pass
2. Update documentation
3. Add any new dependencies to requirements.txt
4. Request review from maintainers

## Code of Conduct

Be respectful and inclusive. We're building something great together!
