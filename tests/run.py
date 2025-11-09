#!/usr/bin/env python3
import subprocess
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def get_current_challenge_index():
    try:
        if os.path.exists('dsa.config.json'):
            with open('dsa.config.json', 'r') as f:
                config = json.load(f)
                return config.get('currentChallengeIndex', 0)
    except Exception as e:
        print(f'Warning: Could not read dsa.config.json: {e}', file=sys.stderr)
    return 0

ALL_TESTS = [
    {'file': 'tests/test_01_create_class.py', 'slug': 'create-class'},
    {'file': 'tests/test_02_enqueue.py', 'slug': 'enqueue'},
    {'file': 'tests/test_03_dequeue.py', 'slug': 'dequeue'},
    {'file': 'tests/test_04_front.py', 'slug': 'front'},
    {'file': 'tests/test_05_size.py', 'slug': 'size'},
]

def run_tests():
    current_challenge_index = get_current_challenge_index()
    
    # Get module ID from config
    module_id = 'unknown'
    try:
        if os.path.exists('dsa.config.json'):
            with open('dsa.config.json', 'r') as f:
                config = json.load(f)
                module_id = config.get('moduleId', 'unknown')
    except Exception:
        pass
    tests_to_run = ALL_TESTS[:current_challenge_index + 1]
    locked_tests = ALL_TESTS[current_challenge_index + 1:]
    
    print(f"Running tests for: {module_id}")
    print(f"Current challenge: {current_challenge_index + 1}/{len(ALL_TESTS)}")
    print()
    
    results = []
    passed_count = 0
    
    env = os.environ.copy()
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env['PYTHONPATH'] = project_root
    
    for test in tests_to_run:
        if not os.path.exists(test['file']):
            print(f"✗ {test['slug']} (file not found)")
            results.append({
                'subchallengeId': test['slug'],
                'passed': False,
                'message': 'Test file not found'
            })
            continue
        
        try:
            subprocess.run(
                ['pytest', test['file'], '-v'],
                check=True,
                capture_output=True,
                text=True,
                env=env
            )
            results.append({'subchallengeId': test['slug'], 'passed': True})
            passed_count += 1
            print(f"✓ {test['slug']}")
        except subprocess.CalledProcessError as e:
            message = e.stderr or e.stdout or 'Test failed'
            results.append({
                'subchallengeId': test['slug'],
                'passed': False,
                'message': message.strip()
            })
            print(f"✗ {test['slug']}")
    
    for test in locked_tests:
        results.append({
            'subchallengeId': test['slug'],
            'passed': False,
            'message': 'Challenge locked'
        })
    
    report = {
        'moduleId': module_id,
        'summary': f"{passed_count}/{len(tests_to_run)} tests passed ({len(locked_tests)} locked)",
        'pass': passed_count == len(tests_to_run),
        'cases': results,
        'currentChallengeIndex': current_challenge_index,
    }
    
    with open('.dsa-report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print()
    print(f"Summary: {report['summary']}")
    sys.exit(0 if report['pass'] else 1)

if __name__ == '__main__':
    try:
        run_tests()
    except Exception as e:
        print(f"Test runner failed: {e}", file=sys.stderr)
        sys.exit(1)
