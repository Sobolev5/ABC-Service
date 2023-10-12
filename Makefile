push:
	ansible-playbook -i ./playbooks/inventory/hosts ./playbooks/push.yml

stack:
	docker compose -f docker-compose.stack.yml up --build -d

backup:
	cd .. && tar -zcvf backup.tar.gz ABC-Service